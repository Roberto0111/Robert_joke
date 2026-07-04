import fs from "node:fs";
import path from "node:path";
import process from "node:process";

const root = process.cwd();
const dryRun = process.argv.includes("--dry-run");
const checkToken = process.argv.includes("--check-token");

loadDotEnv(path.join(root, ".env"));

const apiMode = process.env.IG_API_MODE || "instagram_login";
const graphVersion = process.env.IG_GRAPH_VERSION || "v23.0";
const igUserId = requiredEnv("IG_USER_ID");
const accessToken = requiredEnv("IG_ACCESS_TOKEN");
const imageUrl = requiredEnv("IG_IMAGE_URL");
const captionFile = process.env.IG_CAPTION_FILE || "captions/001_deadpan_nonsense_tuxedo_cat.md";
const caption = fs.readFileSync(path.join(root, captionFile), "utf8").trim();

const baseUrl = getBaseUrl(apiMode, graphVersion);

if (checkToken) {
  const me = await getGraph(`${baseUrl}/me`, {
    fields: "id,username,account_type",
    access_token: accessToken,
  });

  console.log("Instagram token check:");
  console.log(JSON.stringify(me, null, 2));
  process.exit(0);
}

if (dryRun) {
  console.log("Dry run: Instagram publish payload");
  console.log(JSON.stringify({
    apiMode,
    baseUrl,
    igUserId,
    imageUrl,
    caption,
    graphVersion,
  }, null, 2));
  process.exit(0);
}

const container = await postGraph(`${baseUrl}/${igUserId}/media`, {
  image_url: imageUrl,
  caption,
  access_token: accessToken,
});

if (!container.id) {
  throw new Error(`Instagram did not return a media container id: ${JSON.stringify(container)}`);
}

console.log(`Created media container: ${container.id}`);

const publish = await publishWithRetry(`${baseUrl}/${igUserId}/media_publish`, {
  creation_id: container.id,
  access_token: accessToken,
});

console.log("Published Instagram media:");
console.log(JSON.stringify(publish, null, 2));

function getBaseUrl(mode, version) {
  if (mode === "instagram_login") {
    return `https://graph.instagram.com/${version}`;
  }

  if (mode === "facebook_graph") {
    return `https://graph.facebook.com/${version}`;
  }

  throw new Error(`Unsupported IG_API_MODE: ${mode}. Use instagram_login or facebook_graph.`);
}

async function getGraph(url, values) {
  const params = new URLSearchParams(values);
  const response = await fetch(`${url}?${params.toString()}`);
  const data = await response.json().catch(() => ({}));

  if (!response.ok) {
    const message = data.error?.message || response.statusText;
    throw new Error(`Instagram API error ${response.status}: ${message}\n${JSON.stringify(data, null, 2)}`);
  }

  return data;
}

async function postGraph(url, values) {
  const body = new URLSearchParams(values);
  const response = await fetch(url, {
    method: "POST",
    body,
  });

  const data = await response.json().catch(() => ({}));

  if (!response.ok) {
    const message = data.error?.message || response.statusText;
    throw new Error(`Instagram API error ${response.status}: ${message}\n${JSON.stringify(data, null, 2)}`);
  }

  return data;
}

async function publishWithRetry(url, values) {
  const maxAttempts = Number(process.env.IG_PUBLISH_ATTEMPTS || 6);
  const delayMs = Number(process.env.IG_PUBLISH_RETRY_MS || 10000);
  let lastError;

  for (let attempt = 1; attempt <= maxAttempts; attempt += 1) {
    try {
      return await postGraph(url, values);
    } catch (error) {
      lastError = error;
      const message = String(error?.message || error);
      const mediaNotReady = message.includes("Media ID is not available") || message.includes("素材尚未準備好");
      if (!mediaNotReady || attempt === maxAttempts) {
        throw error;
      }
      console.error(`Media not ready; retrying publish in ${Math.round(delayMs / 1000)}s (${attempt}/${maxAttempts})`);
      await sleep(delayMs);
    }
  }

  throw lastError;
}

function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

function requiredEnv(name) {
  const value = process.env[name];
  if (!value) {
    throw new Error(`Missing required environment variable: ${name}`);
  }
  return value;
}

function loadDotEnv(filePath) {
  if (!fs.existsSync(filePath)) {
    return;
  }

  const lines = fs.readFileSync(filePath, "utf8").split(/\r?\n/);
  for (const line of lines) {
    const trimmed = line.trim();
    if (!trimmed || trimmed.startsWith("#")) {
      continue;
    }

    const equals = trimmed.indexOf("=");
    if (equals === -1) {
      continue;
    }

    const key = trimmed.slice(0, equals).trim();
    let value = trimmed.slice(equals + 1).trim();
    if ((value.startsWith('"') && value.endsWith('"')) || (value.startsWith("'") && value.endsWith("'"))) {
      value = value.slice(1, -1);
    }

    if (!process.env[key]) {
      process.env[key] = value;
    }
  }
}
