import fs from "node:fs";
import path from "node:path";

const root = process.cwd();
const analyticsDir = path.join(root, "analytics");
const analyticsPath = path.join(analyticsDir, "latest.json");
if (!fs.existsSync(analyticsPath)) {
  throw new Error(`Analytics file not found: ${analyticsPath}`);
}

const targetFollowers = 1000;
const report = JSON.parse(fs.readFileSync(analyticsPath, "utf8"));
const manifestByMediaId = readManifestIndex(path.join(root, "posts"));
const posts = (report.posts || []).map((post) => ({
  ...post,
  views: number(post.metrics?.views),
  reach: number(post.metrics?.reach),
  shares: number(post.metrics?.shares),
  saves: number(post.metrics?.saved),
  interactions: number(post.metrics?.total_interactions),
  experiment: manifestByMediaId.get(String(post.id))?.growth_experiment || null,
}));

const reels = posts.filter((post) => post.media_product_type === "REELS");
const images = posts.filter((post) => post.media_product_type !== "REELS");
const lifeDialoguePosts = posts.filter((post) => (post.caption || "").includes("#人生對話"));
const comedyPosts = posts.filter((post) => !lifeDialoguePosts.includes(post));
const reelStats = summarize(reels);
const imageStats = summarize(images);
const lifeDialogueStats = summarize(lifeDialoguePosts);
const comedyStats = summarize(comedyPosts);
const followerTrend = readFollowerTrend(analyticsDir, report);
const experimentStats = summarizeExperiments(posts);
const nextExperiment = chooseNextExperiment(experimentStats, report.collected_at);
const best = [...posts].sort((a, b) => postScore(b) - postScore(a))[0];
const currentFollowers = number(report.profile?.followers_count);
const targetGap = Math.max(0, targetFollowers - currentFollowers);
const adReadiness = evaluateAdReadiness(best);

const recommendations = [
  `執行實驗 ${nextExperiment.id}：${nextExperiment.label}。本篇只改指定變因，其餘角色與五頁情緒結構固定。`,
  `首格使用「${nextExperiment.hook_style}」；題材優先「${nextExperiment.topic_pillar}」；Reel ${nextExperiment.reel_seconds} 秒。`,
  "前 1 秒必須已看見人物、賓士貓與完整首句，不使用黑畫面、片頭 Logo 或空鏡。",
];
if (posts.reduce((sum, post) => sum + post.shares, 0) <= 1) {
  recommendations.push("分享訊號太低；選一個觀眾會立刻想到某位朋友的具體尷尬或選擇，不寫泛用人生大道理。");
}
if (posts.reduce((sum, post) => sum + post.saves, 0) === 0) {
  recommendations.push("收藏仍為 0；第五頁必須給可在下次遇到同場景時使用的具體判斷句。");
}
if (followerTrend.delta7d <= 0) {
  recommendations.push("近 7 日粉絲沒有成長；本週優先提高可轉傳性，不用增加發文頻率掩蓋內容問題。");
}
recommendations.push(`Caption 使用「${nextExperiment.cta_style}」收尾；只放 3-5 個精準標籤，不堆熱門但無關的 hashtag。`);
if (adReadiness.ready) {
  recommendations.push("已有自然流量勝出貼文；請 Roberto 核准後才建立小額廣告測試，不會自動扣款。");
}
recommendations.push("每日參考貼文只拆解敘事機制；題目、句子、結論與視覺必須保持 Roberto 原創。");

const strategy = `# Roberto Joke Organic Growth Strategy

Updated: ${new Date().toISOString()}
Account: @${report.profile?.username || "roberto_joke"}
Goal: ${currentFollowers} / ${targetFollowers} followers (gap ${targetGap})
7-day follower change: ${signed(followerTrend.delta7d)}
Phase: organic validation

## Next Controlled Experiment

- ID: ${nextExperiment.id}
- Package: ${nextExperiment.label}
- Hook: ${nextExperiment.hook_style}
- Topic pillar: ${nextExperiment.topic_pillar}
- Conclusion: ${nextExperiment.conclusion_style}
- Reel timing: ${nextExperiment.reel_seconds}s total across five readable pages
- Caption CTA: ${nextExperiment.cta_style}

## Recent Performance

| Format | Samples | Avg views | Avg reach | Views / reach | Interaction rate | Share + save rate |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Reel | ${reelStats.samples} | ${fixed(reelStats.avgViews)} | ${fixed(reelStats.avgReach)} | ${fixed(reelStats.repeatViewRate)} | ${percent(reelStats.engagementRate)} | ${percent(reelStats.shareSaveRate)} |
| Image | ${imageStats.samples} | ${fixed(imageStats.avgViews)} | ${fixed(imageStats.avgReach)} | ${fixed(imageStats.repeatViewRate)} | ${percent(imageStats.engagementRate)} | ${percent(imageStats.shareSaveRate)} |

## Experiment Leaderboard

${experimentTable(experimentStats)}

## Best Recent Post

${best ? `- ${best.permalink}\n- Views ${best.views}, reach ${best.reach}, shares ${best.shares}, saves ${best.saves}\n- Caption: ${(best.caption || "").split("\n").slice(0, 2).join(" / ")}` : "- No post data"}

## Instructions For The Next Post

${recommendations.map((item) => `- ${item}`).join("\n")}

## Paid Promotion Gate

- Ready: ${adReadiness.ready ? "yes" : "no"}
- Reason: ${adReadiness.reason}
- Do not boost a post merely because it has the highest views. Require organic reach >= 500, at least 3 combined shares/saves, and share+save rate >= 1%.
- When the gate passes, test at most two proven Reels in Meta Ads Manager before increasing budget.

## Guardrails

- Keep one primary Reel per day at 20:30; quality and learning matter more than posting volume.
- Keep Roberto, the tuxedo cat, original art, Traditional Chinese, and the five-beat emotional-dialogue identity stable.
- Change one creative package at a time and require at least two samples before declaring a winner.
- Optimize for follower growth, reach, shares, and saves; never buy followers, mass-follow, or automate spam comments/DMs.
- Never copy a winning caption; reuse only the proven abstract structure.
`;

const payload = {
  updated_at: new Date().toISOString(),
  account: report.profile?.username || "roberto_joke",
  phase: "organic_validation",
  summary: `自然成長 ${currentFollowers}/${targetFollowers} 粉；下一篇測試 ${nextExperiment.label}`,
  target_seconds: nextExperiment.reel_seconds,
  cta: nextExperiment.cta_style,
  target_followers: targetFollowers,
  current_followers: currentFollowers,
  target_gap: targetGap,
  follower_change_7d: followerTrend.delta7d,
  projected_days_at_current_7d_rate: followerTrend.delta7d > 0
    ? Math.ceil(targetGap / (followerTrend.delta7d / 7))
    : null,
  reels: reelStats,
  images: imageStats,
  life_dialogue: lifeDialogueStats,
  deadpan_comedy: comedyStats,
  next_experiment: nextExperiment,
  experiment_stats: experimentStats,
  recommendations,
  best_post_id: best?.id || null,
  paid_promotion: adReadiness,
};

fs.writeFileSync(path.join(analyticsDir, "daily_strategy.md"), strategy);
fs.writeFileSync(path.join(analyticsDir, "daily_strategy.json"), `${JSON.stringify(payload, null, 2)}\n`);
fs.mkdirSync(path.join(root, "growth"), { recursive: true });
fs.writeFileSync(
  path.join(root, "growth", "goal_status.json"),
  `${JSON.stringify({
    updated_at: payload.updated_at,
    account: payload.account,
    phase: payload.phase,
    target_followers: targetFollowers,
    current_followers: currentFollowers,
    remaining_followers: targetGap,
    follower_change_7d: followerTrend.delta7d,
    best_recent_post: best ? {
      id: best.id,
      permalink: best.permalink,
      reach: best.reach,
      views: best.views,
      shares: best.shares,
      saves: best.saves,
    } : null,
    next_experiment: nextExperiment,
    paid_promotion: adReadiness,
  }, null, 2)}\n`,
);
const weeklyReport = `# Roberto Joke Weekly Growth Check

Updated: ${payload.updated_at}

- Followers: ${currentFollowers} / ${targetFollowers}
- Seven-day change: ${signed(followerTrend.delta7d)}
- Recent Reel average reach: ${fixed(reelStats.avgReach)}
- Recent share + save rate: ${percent(reelStats.shareSaveRate)}
- Best recent Reel: ${best?.permalink || "none"}
- Next experiment: ${nextExperiment.id} (${nextExperiment.label})
- Paid promotion: ${adReadiness.ready ? "ready for a small controlled test" : "off"}
- Decision: ${adReadiness.reason}

## Human Actions That Cannot Be Safely Automated

- Reply to genuine comments in Roberto's own voice.
- Share the best Reel to Roberto's personal Story when it genuinely fits.
- Approve creator collaborations and any ad spend before money is charged.
- Do not use purchased followers, mass-following, or generic automated comments.
`;
fs.writeFileSync(path.join(root, "growth", "weekly_report.md"), weeklyReport);
console.log(`Joke growth strategy updated: followers=${currentFollowers}/${targetFollowers} experiment=${nextExperiment.id}`);

function experimentCatalog() {
  return [
    {
      id: "A_specific_scene_16",
      label: "具體生活現場",
      hook_style: "直接說出剛發生的具體場景，不先講道理",
      topic_pillar: "金錢、人情與不好意思拒絕",
      conclusion_style: "指出真正付出的隱形成本",
      cta_style: "一句自然的『你也遇過嗎？』",
      reel_seconds: 28,
    },
    {
      id: "B_confession_14",
      label: "不太體面的坦白",
      hook_style: "Roberto 坦白一個不好意思承認的小心思",
      topic_pillar: "比較、面子與社交焦慮",
      conclusion_style: "貓精準拆掉 Roberto 的自我包裝",
      cta_style: "不要求互動，以可轉傳的最後一句收尾",
      reel_seconds: 27,
    },
    {
      id: "C_contradiction_16",
      label: "反常識矛盾",
      hook_style: "用一個看似矛盾但具體的句子製造停留",
      topic_pillar: "休息、拖延與自我要求",
      conclusion_style: "把問題從意志力改寫成選擇成本",
      cta_style: "問觀眾會怎麼選，不暗示標準答案",
      reel_seconds: 28,
    },
    {
      id: "D_relationship_18",
      label: "關係裡的小瞬間",
      hook_style: "從一句真實對話或已讀未回的小場景開始",
      topic_pillar: "友情、界線與害怕失去",
      conclusion_style: "區分關心與勉強維持",
      cta_style: "用一句適合傳給朋友但不情緒勒索的收尾",
      reel_seconds: 30,
    },
    {
      id: "E_cat_dry_turn_14",
      label: "嚴肅中的冷轉折",
      hook_style: "Roberto 很認真地替自己找理由",
      topic_pillar: "消費、飲食、健身與日常自欺",
      conclusion_style: "貓用一點乾幽默說出精準後果",
      cta_style: "短問句，讓觀眾自然想到可分享的人",
      reel_seconds: 27,
    },
    {
      id: "F_decision_tool_18",
      label: "可收藏的判斷工具",
      hook_style: "提出一個大家常拖著不決定的具體選擇",
      topic_pillar: "工作、選擇與放下沉沒成本",
      conclusion_style: "第五頁給一句能在下次使用的判斷問題",
      cta_style: "自然提醒留著下次卡住時看，不硬討收藏",
      reel_seconds: 30,
    },
  ];
}

function chooseNextExperiment(stats, collectedAt) {
  const catalog = experimentCatalog();
  const byId = new Map(stats.map((item) => [item.id, item]));
  const minimumSamples = Math.min(...catalog.map((item) => byId.get(item.id)?.samples || 0));
  const underTested = catalog.filter((item) => (byId.get(item.id)?.samples || 0) === minimumSamples);
  const daySeed = Math.floor(new Date(collectedAt || Date.now()).getTime() / 86400000);

  if (minimumSamples < 2 || daySeed % 4 === 0) {
    return underTested[daySeed % underTested.length];
  }

  return [...catalog].sort((a, b) =>
    (byId.get(b.id)?.quality_score || 0) - (byId.get(a.id)?.quality_score || 0)
  )[0];
}

function summarizeExperiments(items) {
  const groups = new Map();
  for (const post of items) {
    const id = post.experiment?.id;
    if (!id) continue;
    if (!groups.has(id)) groups.set(id, []);
    groups.get(id).push(post);
  }
  return [...groups.entries()].map(([id, grouped]) => {
    const summary = summarize(grouped);
    return {
      id,
      ...summary,
      quality_score: summary.avgReach + summary.shareRate * 2500 + summary.saveRate * 2000 + summary.engagementRate * 250,
    };
  }).sort((a, b) => b.quality_score - a.quality_score);
}

function readManifestIndex(postsDir) {
  const index = new Map();
  if (!fs.existsSync(postsDir)) return index;
  for (const entry of fs.readdirSync(postsDir, { withFileTypes: true })) {
    if (!entry.isDirectory()) continue;
    const manifestPath = path.join(postsDir, entry.name, "manifest.json");
    if (!fs.existsSync(manifestPath)) continue;
    try {
      const manifest = JSON.parse(fs.readFileSync(manifestPath, "utf8"));
      if (manifest.instagram_media_id) index.set(String(manifest.instagram_media_id), manifest);
    } catch {
      // A malformed historical manifest must not stop the daily analytics job.
    }
  }
  return index;
}

function readFollowerTrend(dir, latest) {
  const snapshots = [];
  for (const filename of fs.readdirSync(dir)) {
    if (!/^\d{4}-\d{2}-\d{2}T.*\.json$/.test(filename)) continue;
    try {
      const data = JSON.parse(fs.readFileSync(path.join(dir, filename), "utf8"));
      const timestamp = Date.parse(data.collected_at);
      if (Number.isFinite(timestamp)) snapshots.push({ timestamp, followers: number(data.profile?.followers_count) });
    } catch {
      // Ignore one bad snapshot and preserve the remaining history.
    }
  }
  const latestPoint = { timestamp: Date.parse(latest.collected_at) || Date.now(), followers: number(latest.profile?.followers_count) };
  snapshots.push(latestPoint);
  snapshots.sort((a, b) => a.timestamp - b.timestamp);
  const cutoff = latestPoint.timestamp - 7 * 86400000;
  const baseline = snapshots.find((item) => item.timestamp >= cutoff) || snapshots[0] || latestPoint;
  return { delta7d: latestPoint.followers - baseline.followers };
}

function evaluateAdReadiness(post) {
  if (!post) return { ready: false, reason: "尚無可評估貼文。" };
  const shareSaveRate = post.reach ? (post.shares + post.saves) / post.reach : 0;
  const ready = post.reach >= 500 && post.shares + post.saves >= 3 && shareSaveRate >= 0.01;
  return {
    ready,
    candidate_media_id: ready ? post.id : null,
    reason: ready
      ? `自然觸及 ${post.reach}，分享＋收藏 ${post.shares + post.saves}，已通過小額廣告測試門檻。`
      : `目前最佳自然觸及 ${post.reach}、分享＋收藏 ${post.shares + post.saves}；先改善內容，不投廣告。`,
  };
}

function experimentTable(stats) {
  if (!stats.length) return "尚未累積帶實驗標籤的貼文；從下一篇開始記錄。";
  const rows = stats.map((item) => `| ${item.id} | ${item.samples} | ${fixed(item.avgReach)} | ${percent(item.shareRate)} | ${percent(item.saveRate)} | ${fixed(item.quality_score)} |`);
  return [
    "| Experiment | Samples | Avg reach | Share rate | Save rate | Quality score |",
    "| --- | ---: | ---: | ---: | ---: | ---: |",
    ...rows,
  ].join("\n");
}

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
    shareSaveRate: reach ? (shares + saves) / reach : 0,
  };
}

function postScore(post) {
  return post.reach + post.views * 0.1 + post.shares * 30 + post.saves * 25 + post.interactions * 4;
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

function signed(value) {
  return value > 0 ? `+${value}` : String(value);
}
