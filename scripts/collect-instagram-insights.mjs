import fs from "node:fs";
import path from "node:path";
import process from "node:process";

const root = process.cwd();
loadDotEnv(path.join(root, ".env"));

const apiMode = process.env.IG_API_MODE || "instagram_login";
const graphVersion = process.env.IG_GRAPH_VERSION || "v23.0";
const igUserId = requiredEnv("IG_USER_ID");
const accessToken = requiredEnv("IG_ACCESS_TOKEN");
const baseUrl = apiMode === "facebook_graph"
  ? `https://graph.facebook.com/${graphVersion}`
  : `https://graph.instagram.com/${graphVersion}`;

const profile = await getGraph(`${baseUrl}/${igUserId}`, {
  fields: "id,username,name,biography,account_type,media_count,followers_count,follows_count",
  access_token: accessToken,
});
const media = await getGraph(`${baseUrl}/${igUserId}/media`, {
  fields: "id,caption,media_type,media_product_type,permalink,timestamp,like_count,comments_count",
  limit: "15",
  access_token: accessToken,
});

const posts = [];
for (const item of media.data || []) {
  const insights = await getGraph(`${baseUrl}/${item.id}/insights`, {
    metric: "views,reach,saved,shares,total_interactions",
    access_token: accessToken,
  });
  const metrics = Object.fromEntries(
    (insights.data || []).map((entry) => [entry.name, entry.values?.[0]?.value ?? 0]),
  );
  posts.push({ ...item, metrics });
}

const now = new Date();
const report = {
  collected_at: now.toISOString(),
  profile,
  posts,
};
const analyticsDir = path.join(root, "analytics");
fs.mkdirSync(analyticsDir, { recursive: true });
const stamp = now.toISOString().replace(/[:.]/g, "-");
fs.writeFileSync(path.join(analyticsDir, `${stamp}.json`), `${JSON.stringify(report, null, 2)}\n`);
fs.writeFileSync(path.join(analyticsDir, "latest.json"), `${JSON.stringify(report, null, 2)}\n`);

console.log(JSON.stringify({
  collected_at: report.collected_at,
  username: profile.username,
  followers_count: profile.followers_count,
  media_count: profile.media_count,
  posts_collected: posts.length,
}, null, 2));

async function getGraph(url, values) {
  const params = new URLSearchParams(values);
  const response = await fetch(`${url}?${params.toString()}`);
  const data = await response.json().catch(() => ({}));
  if (!response.ok) {
    const message = data.error?.message || response.statusText;
    throw new Error(`Instagram API error ${response.status}: ${message}`);
  }
  return data;
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
  for (const line of fs.readFileSync(filePath, "utf8").split(/\r?\n/)) {
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
