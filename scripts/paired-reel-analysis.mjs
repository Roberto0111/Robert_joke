const MIN_AGE_HOURS = 18;
const MIN_REACH_RATIO = 1.5;

export function analyzePairedReels(posts, collectedAt = new Date().toISOString()) {
  const now = Date.parse(collectedAt) || Date.now();
  const reels = posts
    .filter((post) => post.media_product_type === "REELS")
    .filter((post) => ageHours(post, now) >= MIN_AGE_HOURS)
    .filter((post) => metric(post, "reach") > 0);

  if (reels.length < 2) {
    return insufficient("至少需要兩支發布滿 18 小時且有觸及資料的 Reel。");
  }

  const candidates = [];
  for (let left = 0; left < reels.length; left += 1) {
    for (let right = left + 1; right < reels.length; right += 1) {
      const a = reels[left];
      const b = reels[right];
      if (seriesOf(a) !== seriesOf(b)) continue;
      const winner = metric(a, "reach") >= metric(b, "reach") ? a : b;
      const loser = winner === a ? b : a;
      const ratio = metric(winner, "reach") / Math.max(1, metric(loser, "reach"));
      if (ratio < MIN_REACH_RATIO) continue;
      const similarity = pairSimilarity(winner, loser);
      candidates.push({ winner, loser, ratio, similarity, score: ratio * (0.7 + similarity) });
    }
  }

  if (!candidates.length) {
    return insufficient("目前沒有同系列且觸及差距達 1.5 倍的成熟 Reel，不強行解讀雜訊。");
  }

  const pair = candidates.sort((a, b) => b.score - a.score)[0];
  const winnerFeatures = hookFeatures(pair.winner);
  const loserFeatures = hookFeatures(pair.loser);
  const diagnoses = diagnose(pair, winnerFeatures, loserFeatures);
  return {
    status: "ready",
    comparison_basis: "同系列、發布至少 18 小時、觸及差距至少 1.5 倍",
    confidence: confidence(pair),
    reach_ratio: round(pair.ratio, 2),
    similarity_score: round(pair.similarity, 3),
    winner: postSummary(pair.winner, winnerFeatures),
    loser: postSummary(pair.loser, loserFeatures),
    diagnoses,
    next_test: nextTest(diagnoses, winnerFeatures),
    caution: "這是相關性診斷，不把單一差異宣稱為演算法因果。下一篇只測一個變因。",
  };
}

function insufficient(reason) {
  return { status: "insufficient_sample", reason, diagnoses: [], next_test: "維持現有格式並繼續累積成熟樣本。" };
}

function diagnose(pair, winner, loser) {
  const results = [];
  if (winner.type !== loser.type) {
    const descriptions = {
      question: "勝出片用觀眾會在心裡回答的問題開場",
      contrast: "勝出片先給反差或矛盾，再解釋原因",
      confession: "勝出片先承認一個不太體面的具體感受",
      numeric: "勝出片先交代一個可理解的關鍵數字",
      statement: "勝出片使用直接、具體的陳述開場",
    };
    results.push(`${descriptions[winner.type]}；下一篇可單獨重測這種首句。`);
  }
  if (winner.length + 6 < loser.length) {
    results.push(`勝出片首句較短（${winner.length} vs ${loser.length} 字），可能降低第一秒閱讀負擔。`);
  }
  const winnerWatch = metric(pair.winner, "ig_reels_avg_watch_time");
  const loserWatch = metric(pair.loser, "ig_reels_avg_watch_time");
  if (winnerWatch && loserWatch && winnerWatch >= loserWatch * 1.2) {
    results.push(`勝出片平均觀看時間高 ${Math.round((winnerWatch / loserWatch - 1) * 100)}%，節奏或資訊揭露順序值得保留。`);
  } else if (pair.ratio >= 2 && winnerWatch && loserWatch && winnerWatch <= loserWatch * 1.05) {
    results.push("觸及差距很大但觀看時間沒有同步提高，較可能是題材或封面分發差異，暫不重做整支影片節奏。");
  }
  const winnerAction = actionRate(pair.winner);
  const loserAction = actionRate(pair.loser);
  if (winnerAction >= loserAction + 0.005) {
    results.push(`勝出片分享收藏率較高（${percent(winnerAction)} vs ${percent(loserAction)}），結論的可轉傳性比單純觀看更強。`);
  }
  if (!results.length) {
    results.push("目前只能確認觸及落差，首句、觀看與分享收藏沒有足夠差異；下一篇先複測，不做大改版。");
  }
  return results;
}

function nextTest(diagnoses, features) {
  if (diagnoses.some((item) => item.includes("首句") || item.includes("開場"))) {
    return `下一篇只測「${hookLabel(features.type)}」首句，其餘五頁結構、片長與 CTA 保持不變。`;
  }
  if (diagnoses.some((item) => item.includes("沒有同步提高"))) {
    return "下一篇固定目前節奏與 CTA，只測一個新的題材或封面主張。";
  }
  if (diagnoses.some((item) => item.includes("觀看時間"))) {
    return "下一篇沿用勝出片的資訊揭露節奏，只更換題材，不同時修改 CTA。";
  }
  if (diagnoses.some((item) => item.includes("分享收藏率"))) {
    return "下一篇保留可傳給特定朋友的收束方式，只測新的具體生活情境。";
  }
  return "下一篇維持現有格式，只測一個新的第一頁鉤子。";
}

function hookFeatures(post) {
  const firstLine = String(post.caption || "").split("\n").find((line) => line.trim())?.trim() || "";
  let type = "statement";
  if (/[？?]/.test(firstLine)) type = "question";
  else if (/不是|但|卻|其實|反而|明明|沒想到/.test(firstLine)) type = "contrast";
  else if (/^我|有時候|不敢|害怕|怕/.test(firstLine)) type = "confession";
  else if (/\d/.test(firstLine)) type = "numeric";
  return { first_line: firstLine, type, length: [...firstLine].length };
}

function pairSimilarity(a, b) {
  let score = seriesOf(a) === seriesOf(b) ? 0.55 : 0;
  if (a.experiment?.id && a.experiment.id === b.experiment?.id) score += 0.25;
  score += 0.2 * jaccard(bigrams(String(a.caption || "")), bigrams(String(b.caption || "")));
  return Math.min(1, score);
}

function seriesOf(post) {
  return post.series || (String(post.caption || "").includes("#人生對話") ? "life_dialogue" : "deadpan_comedy");
}

function bigrams(value) {
  const compact = value.replace(/\s+/g, "").slice(0, 120);
  const result = new Set();
  for (let index = 0; index < compact.length - 1; index += 1) result.add(compact.slice(index, index + 2));
  return result;
}

function jaccard(a, b) {
  if (!a.size || !b.size) return 0;
  const intersection = [...a].filter((item) => b.has(item)).length;
  return intersection / (a.size + b.size - intersection);
}

function postSummary(post, features) {
  return {
    id: post.id,
    permalink: post.permalink,
    timestamp: post.timestamp,
    series: seriesOf(post),
    first_line: features.first_line,
    hook_type: features.type,
    reach: metric(post, "reach"),
    views: metric(post, "views"),
    avg_watch_time_ms: metric(post, "ig_reels_avg_watch_time"),
    shares: metric(post, "shares"),
    saves: metric(post, "saved") || Number(post.saves || 0),
  };
}

function ageHours(post, now) {
  const timestamp = Date.parse(post.timestamp);
  return Number.isFinite(timestamp) ? (now - timestamp) / 3600000 : 0;
}

function metric(post, name) {
  const direct = post[name];
  const nested = post.metrics?.[name];
  return Number.isFinite(Number(direct ?? nested)) ? Number(direct ?? nested) : 0;
}

function actionRate(post) {
  const reach = metric(post, "reach");
  const saves = metric(post, "saved") || Number(post.saves || 0);
  return reach ? (metric(post, "shares") + saves) / reach : 0;
}

function confidence(pair) {
  if (pair.ratio >= 3 && pair.similarity >= 0.7) return "high";
  if (pair.ratio >= 2 && pair.similarity >= 0.55) return "medium";
  return "exploratory";
}

function hookLabel(type) {
  return { question: "觀眾問題", contrast: "反差矛盾", confession: "真實坦白", numeric: "關鍵數字", statement: "直接陳述" }[type] || "直接陳述";
}

function percent(value) {
  return `${(value * 100).toFixed(1)}%`;
}

function round(value, digits) {
  return Number(value.toFixed(digits));
}
