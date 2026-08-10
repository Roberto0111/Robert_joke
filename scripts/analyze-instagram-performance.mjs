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
const recommendedFormat = "reel";
const formatReason = "The account is fixed to the daily serious life-dialogue Reel format; data adjusts pacing and topics only.";
const recommendedContentMode = "life_dialogue";
const contentModeConfident = true;
const contentModeReason = "帳號內容已固定為人生對話；數據只調整格式、節奏與包裝，不切換內容支柱。";

const best = [...posts].sort((a, b) =>
  (b.shares * 5 + b.saves * 4 + b.reach + b.views * 0.1)
  - (a.shares * 5 + a.saves * 4 + a.reach + a.views * 0.1)
)[0];

const recommendations = [];
recommendations.push("固定發布 16 秒人生對話 Reel；保留兩張四格原稿，成效數據只用來調整題材、開場與閱讀節奏。");
if (posts.reduce((sum, post) => sum + post.shares, 0) === 0) {
  recommendations.push("近期分享為 0；下一篇從觀眾會想到某位朋友的具體困境開始，避免空泛人生大道理。");
}
if (posts.reduce((sum, post) => sum + post.saves, 0) === 0) {
  recommendations.push("近期收藏為 0；第四格要提供一個日後能重新想起來的具體視角，不寫通用勵志標語。");
}
if (reelStats.repeatViewRate >= 1.1) {
  recommendations.push("Reel 每位觸及產生超過 1.1 次觀看；保留兩頁依序揭曉與 16 秒閱讀節奏。");
}
if (reelStats.engagementRate === 0) {
  recommendations.push("Reel 有觸及但尚無互動；貓的結論要更短、更具體，caption 不重複解釋第四格。");
}
recommendations.push("內容固定為人生對話；持續比較題材、開場與第四格觀點，但不因短期數據切回喜劇模式。");
recommendations.push("每日參考貼文只拆解敘事機制；題目、句子、結論與視覺必須保持 Roberto 原創。");

const strategy = `# Life Dialogue Daily Growth Strategy

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

- Content recommendation: ${recommendedContentMode}
- Reason: ${contentModeReason}

## Best Recent Post

${best ? `- ${best.permalink}
- Views ${best.views}, reach ${best.reach}, shares ${best.shares}, saves ${best.saves}
- Caption: ${(best.caption || "").split("\n").slice(0, 2).join(" / ")}` : "- No post data"}

## Instructions For The Next Post

${recommendations.map((item) => `- ${item}`).join("\n")}

## Publishing Decision

- Recommended format: ${recommendedFormat}
- Reason: ${formatReason}

## Guardrails

- Treat fewer than 3 posts in a format as an early signal, not a conclusion.
- Optimize for non-follower reach, shares, saves, and repeat views before likes.
- Never copy a winning caption; reuse only the proven pacing or dialogue structure.
- Analytics must not change the fixed life_dialogue content mode.
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
