import assert from "node:assert/strict";
import { analyzePairedReels } from "./paired-reel-analysis.mjs";

const collectedAt = "2026-08-19T20:00:00+08:00";

function reel({ id, timestamp = "2026-08-18T00:00:00+08:00", series = "life_dialogue", caption, reach, watch = 0 }) {
  return {
    id,
    timestamp,
    series,
    caption,
    media_product_type: "REELS",
    metrics: {
      reach,
      views: reach + 5,
      shares: 0,
      saved: 0,
      ig_reels_avg_watch_time: watch,
    },
  };
}

{
  const result = analyzePairedReels([
    reel({ id: "old", caption: "其實我不是不努力", reach: 120 }),
    reel({ id: "fresh", timestamp: "2026-08-19T10:00:00+08:00", caption: "今天也很努力", reach: 10 }),
  ], collectedAt);
  assert.equal(result.status, "insufficient_sample");
}

{
  const result = analyzePairedReels([
    reel({ id: "joke", series: "life_dialogue", caption: "不是我不努力，是床太會留人", reach: 180 }),
    reel({ id: "stock", series: "market_brief", caption: "今天市場震盪", reach: 30 }),
  ], collectedAt);
  assert.equal(result.status, "insufficient_sample");
}

{
  const result = analyzePairedReels([
    reel({ id: "winner", caption: "不是我放不下，是已讀不回太有續集感", reach: 180, watch: 6200 }),
    reel({ id: "loser", caption: "我今天想談談人際關係", reach: 60, watch: 3200 }),
  ], collectedAt);
  assert.equal(result.status, "ready");
  assert.equal(result.winner.id, "winner");
  assert.equal(result.reach_ratio, 3);
  assert.equal(result.winner.hook_type, "contrast");
  assert.match(result.next_test, /反差矛盾/);
}

console.log("paired Reel analysis tests passed");
