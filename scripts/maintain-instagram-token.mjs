import fs from "node:fs";
import path from "node:path";
import process from "node:process";

const root = process.cwd();
const envPath = path.join(root, ".env");
const statePath = path.join(root, ".token_refresh_state.json");
const refreshIntervalMs = Number(process.env.IG_TOKEN_REFRESH_DAYS || 7) * 24 * 60 * 60 * 1000;

const env = readDotEnv(envPath);
const apiMode = env.IG_API_MODE || "instagram_login";
const graphVersion = env.IG_GRAPH_VERSION || "v23.0";
const accessToken = required(env, "IG_ACCESS_TOKEN");
const expectedUserId = required(env, "IG_USER_ID");
const baseUrl = apiMode === "facebook_graph"
  ? `https://graph.facebook.com/${graphVersion}`
  : `https://graph.instagram.com/${graphVersion}`;

const account = await getJson(`${baseUrl}/me`, {
  fields: "id,username,account_type",
  access_token: accessToken,
});

if (String(account.id) !== String(expectedUserId)) {
  throw new Error(
    `Instagram token belongs to account ${account.username || account.id}, ` +
    `not configured IG_USER_ID ${expectedUserId}`,
  );
}

console.log(`Instagram token valid for @${account.username || account.id}.`);

if (apiMode !== "instagram_login") {
  console.log("Automatic refresh skipped for Facebook Graph API mode.");
  process.exit(0);
}

const state = readJson(statePath);
const lastRefresh = Date.parse(state.last_refresh_at || "");
if (Number.isFinite(lastRefresh) && Date.now() - lastRefresh < refreshIntervalMs) {
  console.log(`Instagram token refresh not due; last refreshed ${state.last_refresh_at}.`);
  process.exit(0);
}

try {
  const refreshed = await getJson("https://graph.instagram.com/refresh_access_token", {
    grant_type: "ig_refresh_token",
    access_token: accessToken,
  });
  if (!refreshed.access_token) {
    throw new Error("Instagram refresh response did not include an access token");
  }
  replaceDotEnvValue(envPath, "IG_ACCESS_TOKEN", refreshed.access_token);
  const nextState = {
    last_refresh_at: new Date().toISOString(),
    username: account.username || "",
    expires_in_seconds: Number(refreshed.expires_in || 0),
  };
  fs.writeFileSync(statePath, `${JSON.stringify(nextState, null, 2)}\n`, { mode: 0o600 });
  const days = nextState.expires_in_seconds
    ? Math.round((nextState.expires_in_seconds / 86400) * 10) / 10
    : "unknown";
  console.log(`Instagram token refreshed; expires in about ${days} days.`);
} catch (error) {
  // New tokens may be too young to refresh. The identity check already proved
  // the token is usable, so publishing can continue and retry tomorrow.
  console.warn(`Instagram token refresh deferred: ${safeMessage(error)}`);
}

function required(values, key) {
  const value = values[key];
  if (!value) throw new Error(`Missing required environment variable: ${key}`);
  return value;
}

async function getJson(url, values) {
  const params = new URLSearchParams(values);
  const response = await fetch(`${url}?${params.toString()}`);
  const data = await response.json().catch(() => ({}));
  if (!response.ok) {
    const details = data.error || {};
    const code = details.code ? ` code=${details.code}` : "";
    const subcode = details.error_subcode ? ` subcode=${details.error_subcode}` : "";
    throw new Error(`Instagram API ${response.status}${code}${subcode}: ${details.message || response.statusText}`);
  }
  return data;
}

function readDotEnv(filePath) {
  if (!fs.existsSync(filePath)) throw new Error(`Environment file not found: ${filePath}`);
  const values = {};
  for (const line of fs.readFileSync(filePath, "utf8").split(/\r?\n/)) {
    const trimmed = line.trim();
    if (!trimmed || trimmed.startsWith("#") || !trimmed.includes("=")) continue;
    const equals = trimmed.indexOf("=");
    const key = trimmed.slice(0, equals).trim();
    let value = trimmed.slice(equals + 1).trim();
    if ((value.startsWith('"') && value.endsWith('"')) || (value.startsWith("'") && value.endsWith("'"))) {
      value = value.slice(1, -1);
    }
    values[key] = value;
  }
  return values;
}

function replaceDotEnvValue(filePath, key, value) {
  const mode = fs.statSync(filePath).mode;
  const lines = fs.readFileSync(filePath, "utf8").split(/\r?\n/);
  let replaced = false;
  const output = lines.map((line) => {
    if (!line.trim().startsWith("#") && line.match(new RegExp(`^\\s*${key}\\s*=`))) {
      replaced = true;
      return `${key}=${value}`;
    }
    return line;
  });
  if (!replaced) output.push(`${key}=${value}`);
  fs.writeFileSync(filePath, output.join("\n"), { mode });
}

function readJson(filePath) {
  try {
    return JSON.parse(fs.readFileSync(filePath, "utf8"));
  } catch {
    return {};
  }
}

function safeMessage(error) {
  return String(error?.message || error).replace(/access_token=[^&\s]+/gi, "access_token=<redacted>");
}
