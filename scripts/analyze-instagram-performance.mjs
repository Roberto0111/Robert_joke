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
const lifeDialoguePosts = posts.filter((post) => (post.caption || "").includes("#人生對話"));
const comedyPosts = posts.filter((post) => !lifeDialoguePosts.includes(post));
const reelStats = summarize(reels);
const imageStats = summarize(images);
const lifeDialogueStats = summarize(lifeDialoguePosts);
const comedyStats = summarize(comedyPosts);
const reelReachAdvantage = imageStats.avgReach > 0
  ? reelStats.avgReach / imageStats.avgReach
  : reelStats.avgReach > 0 ? Number.POSITIVE_INFINITY : 0;
const imageReachAdvantage = reelStats.avgReach > 0
  ? imageStats.avgReach / reelStats.avgReach
  : imageStats.avgReach > 0 ? Number.POSITIVE_INFINITY : 0;
let recommendedFormat = null;
let formatReason = "Not enough evidence; use the fallback four-Reel schedule.";
let recommendedContentMode = null;
let contentModeConfident = false;
let contentModeReason = "兩種內容各累積至少 3 篇前，維持週三、週日人生對話。";

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

if (lifeDialogueStats.samples >= 3 && comedyStats.samples >= 3) {
  const lifeQuality = contentQuality(lifeDialogueStats);
  const comedyQuality = contentQuality(comedyStats);
  if (lifeQuality > 0 && lifeQuality >= comedyQuality * 1.25 && lifeDialogueStats.avgReach >= comedyStats.avgReach * 0.7) {
    recommendedContentMode = "life_dialogue";
    contentModeConfident = true;
    contentModeReason = "人生對話的分享收藏效率明顯較高，且觸及沒有大幅落後。";
  } else if (comedyQuality > 0 && comedyQuality >= lifeQuality * 1.25 && comedyStats.avgReach >= lifeDialogueStats.avgReach * 0.7) {
    recommendedContentMode = "deadpan_comedy";
    contentModeConfident = true;
    contentModeReason = "認真講幹話的分享收藏效率明顯較高，且觸及沒有大幅落後。";
  } else {
    contentModeReason = "兩種內容表現接近，維持每週兩篇人生對話的混合排程。";
  }
}
const best = [...posts].sort((a, b) =>
  (b.shares * 5 + b.saves * 4 + b.reach + b.views * 0.1)
  - (a.shares * 5 + a.saves * 4 + a.reach + a.views * 0.1)
)[0];

const recommendations = [];
if (recommendedFormat === "reel") {
  recommendations.push("Reel 觸及明顯高於輪播；優先把同一則四格故事做成 12 秒 Reel，但仍保留兩張輪播原稿。");
} else if (recommendedFormat === "image") {
  recommendations.push("輪播觸及已明顯高於 Reel；下一篇直接發布兩張四格 carousel，驗證滑動與分享表現。");
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
  recommendations.push("Reel 每位觸及產生超過 1.1 次觀看；保留兩頁依序揭曉與 12 秒片長。");
}
if (reelStats.engagementRate === 0) {
  recommendations.push("Reel 有觸及但尚無互動；貓的下句要更短、更具體、更能讓主角丟臉，caption 不解釋笑點。");
}
if (contentModeConfident && recommendedContentMode === "life_dialogue") {
  recommendations.push("人生對話的分享收藏效率較好；下週增加到三篇，但保留四篇喜劇維持帳號辨識度。");
} else if (contentModeConfident && recommendedContentMode === "deadpan_comedy") {
  recommendations.push("認真講幹話的分享收藏效率較好；人生對話先縮到週日一篇，持續保留測試樣本。");
} else {
  recommendations.push("內容支柱樣本尚未拉開差距；維持週三、週日人生對話，其餘五天認真講幹話。");
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

## Content Pillar Comparison

| Pillar | Samples | Avg reach | Share rate | Save rate |
| --- | ---: | ---: | ---: | ---: |
| 人生對話 | ${lifeDialogueStats.samples} | ${fixed(lifeDialogueStats.avgReach)} | ${percent(lifeDialogueStats.shareRate)} | ${percent(lifeDialogueStats.saveRate)} |
| 認真講幹話 | ${comedyStats.samples} | ${fixed(comedyStats.avgReach)} | ${percent(comedyStats.shareRate)} | ${percent(comedyStats.saveRate)} |

- Content recommendation: ${recommendedContentMode || "mixed rotation"}
- Reason: ${contentModeReason}

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
    life_dialogue: lifeDialogueStats,
    deadpan_comedy: comedyStats,
    recommended_content_mode: recommendedContentMode,
    content_mode_confident: contentModeConfident,
    content_mode_reason: contentModeReason,
    best_post_id: best?.id || null,
  }, null, 2)}\n`,
);
console.log(`Joke strategy updated: reels=${reels.length} images=${images.length}`);

function summarize(items) {
  const samples = items.length;
  const views = sum(items, "views");
  const reach = sum(items, "reach");
  const interactions = sum(items, "interactions");
  const shares = sum(items, "shares");
  const saves = sum(items, "saves");
  return {
    samples,
    avgViews: samples ? views / samples : 0,
    avgReach: samples ? reach / samples : 0,
    repeatViewRate: reach ? views / reach : 0,
    engagementRate: reach ? interactions / reach : 0,
    shares,
    saves,
    shareRate: reach ? shares / reach : 0,
    saveRate: reach ? saves / reach : 0,
  };
}

function contentQuality(stats) {
  return stats.shareRate * 0.6 + stats.saveRate * 0.4;
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
