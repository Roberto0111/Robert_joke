import fs from "node:fs";
import path from "node:path";

const root = process.cwd();
const analyticsPath = path.join(root, "analytics", "latest.json");
if (!fs.existsSync(analyticsPath)) {
  throw new Error(`Analytics file not found: ${analyticsPath}`);
}

const report = JSON.parse(fs.readFileSync(analyticsPath, "utf8"));
const posts = (report.posts || []).map((post) => ({
  ...post,
  views: number(post.metrics?.views),
  reach: number(post.metrics?.reach),
  shares: number(post.metrics?.shares),
  saves: number(post.metrics?.saved),
  interactions: number(post.metrics?.total_interactions),
}));

const reels = posts.filter((post) => post.media_product_type === "REELS");
const images = posts.filter((post) => post.media_product_type !== "REELS");
const reelStats = summarize(reels);
const imageStats = summarize(images);
const reelReachAdvantage = imageStats.avgReach > 0
  ? reelStats.avgReach / imageStats.avgReach
  : reelStats.avgReach > 0 ? Number.POSITIVE_INFINITY : 0;
const imageReachAdvantage = reelStats.avgReach > 0
  ? imageStats.avgReach / reelStats.avgReach
  : imageStats.avgReach > 0 ? Number.POSITIVE_INFINITY : 0;
let recommendedFormat = null;
let formatReason = "Not enough evidence; use the fallback four-Reel schedule.";

if (
  (reelStats.samples >= 3 && reelReachAdvantage >= 2)
  || (reelStats.samples >= 2 && reelReachAdvantage >= 5)
) {
  recommendedFormat = "reel";
  formatReason = `Reel average reach is ${fixed(reelReachAdvantage)}x image reach.`;
} else if (imageStats.samples >= 3 && imageReachAdvantage >= 1.5) {
  recommendedFormat = "image";
  formatReason = `Image average reach is ${fixed(imageReachAdvantage)}x Reel reach.`;
}
const best = [...posts].sort((a, b) =>
  (b.shares * 5 + b.saves * 4 + b.reach + b.views * 0.1)
  - (a.shares * 5 + a.saves * 4 + a.reach + a.views * 0.1)
)[0];

const recommendations = [];
if (recommendedFormat === "reel") {
  recommendations.push("Reel 觸及明顯高於靜態圖；成長模式每日優先發布 Reel，靜態圖只作為 Reel 素材。");
} else if (recommendedFormat === "image") {
  recommendations.push("靜態圖觸及已明顯高於 Reel；下一篇改用方形圖片驗證是否持續。");
} else if (reels.length < 3) {
  recommendations.push("Reel 樣本仍少於 3 支；先維持目前比例，不因單篇結果大改排程。");
}
if (posts.reduce((sum, post) => sum + post.shares, 0) === 0) {
  recommendations.push("近期分享為 0；下一篇優先寫成能讓觀眾傳給特定朋友的日常情境，避免抽象人生大道理。");
}
if (posts.reduce((sum, post) => sum + post.saves, 0) === 0) {
  recommendations.push("近期收藏為 0；Joke 不硬做知識型收藏，改強化反轉揭曉與重播動機。");
}
if (reelStats.repeatViewRate >= 1.1) {
  recommendations.push("Reel 每位觸及產生超過 1.1 次觀看；保留 3.2 秒揭曉結構與 8 秒片長。");
}
if (reelStats.engagementRate === 0) {
  recommendations.push("Reel 有觸及但尚無互動；貓的下句要更短、更具體、更能讓主角丟臉，caption 不解釋笑點。");
}

const strategy = `# Joke Daily Growth Strategy

Updated: ${new Date().toISOString()}
Account: @${report.profile?.username || "roberto_joke"}
Followers: ${number(report.profile?.followers_count)}

## Format Comparison

| Format | Samples | Avg views | Avg reach | Views / reach | Interaction rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| Reel | ${reelStats.samples} | ${fixed(reelStats.avgViews)} | ${fixed(reelStats.avgReach)} | ${fixed(reelStats.repeatViewRate)} | ${percent(reelStats.engagementRate)} |
| Image | ${imageStats.samples} | ${fixed(imageStats.avgViews)} | ${fixed(imageStats.avgReach)} | ${fixed(imageStats.repeatViewRate)} | ${percent(imageStats.engagementRate)} |

## Best Recent Post

${best ? `- ${best.permalink}
- Views ${best.views}, reach ${best.reach}, shares ${best.shares}, saves ${best.saves}
- Caption: ${(best.caption || "").split("\n").slice(0, 2).join(" / ")}` : "- No post data"}

## Instructions For The Next Post

${recommendations.map((item) => `- ${item}`).join("\n")}

## Publishing Decision

- Recommended format: ${recommendedFormat || "fallback schedule"}
- Reason: ${formatReason}

## Guardrails

- Treat fewer than 3 posts in a format as an early signal, not a conclusion.
- Optimize for non-follower reach, shares, saves, and repeat views before likes.
- Never copy a winning caption; reuse only the proven pacing or joke mechanism.
`;

fs.writeFileSync(path.join(root, "analytics", "daily_strategy.md"), strategy);
fs.writeFileSync(
  path.join(root, "analytics", "daily_strategy.json"),
  `${JSON.stringify({
    updated_at: new Date().toISOString(),
    followers: number(report.profile?.followers_count),
    reels: reelStats,
    images: imageStats,
    recommended_format: recommendedFormat,
    format_reason: formatReason,
    recommendations,
    best_post_id: best?.id || null,
  }, null, 2)}\n`,
);
console.log(`Joke strategy updated: reels=${reels.length} images=${images.length}`);

function summarize(items) {
  const samples = items.length;
  const views = sum(items, "views");
  const reach = sum(items, "reach");
  const interactions = sum(items, "interactions");
  return {
    samples,
    avgViews: samples ? views / samples : 0,
    avgReach: samples ? reach / samples : 0,
    repeatViewRate: reach ? views / reach : 0,
    engagementRate: reach ? interactions / reach : 0,
    shares: sum(items, "shares"),
    saves: sum(items, "saves"),
  };
}

function sum(items, key) {
  return items.reduce((total, item) => total + number(item[key]), 0);
}

function number(value) {
  return Number.isFinite(Number(value)) ? Number(value) : 0;
}

function fixed(value) {
  return Number(value || 0).toFixed(2);
}

function percent(value) {
  return `${(Number(value || 0) * 100).toFixed(1)}%`;
}
