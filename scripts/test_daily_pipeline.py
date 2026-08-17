#!/usr/bin/env python3
from __future__ import annotations

import unittest

import run_daily_pipeline as pipeline


class DailyPipelineTests(unittest.TestCase):
    def test_run_paths_builds_five_ordered_carousel_pages(self) -> None:
        paths = pipeline.run_paths("2026-08-17_2030")
        self.assertEqual(len(paths["images"]), 5)
        self.assertEqual(paths["images"][0].name, "2026-08-17_2030_deadpan_joke_01.png")
        self.assertEqual(paths["images"][-1].name, "2026-08-17_2030_deadpan_joke_05.png")

    def test_reel_timing_keeps_every_page_readable(self) -> None:
        paths = pipeline.run_paths("test")
        paths["growth_experiment"] = {"reel_seconds": 28}
        total, durations = pipeline.reel_timing(paths)
        self.assertEqual(total, 28)
        self.assertEqual(len(durations), 5)
        self.assertAlmostEqual(sum(durations), 28, places=2)
        self.assertGreaterEqual(min(durations), 5)
        self.assertGreater(durations[-1], durations[0])

    def test_reel_filter_concatenates_all_five_pages(self) -> None:
        graph = pipeline.build_reel_filter_graph((5.0, 5.5, 5.5, 5.5, 6.0))
        self.assertIn("[v0][v1][v2][v3][v4]concat=n=5", graph)


if __name__ == "__main__":
    unittest.main()
