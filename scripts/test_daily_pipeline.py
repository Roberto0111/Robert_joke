#!/usr/bin/env python3
from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from unittest import mock

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

    def test_comic_mood_selects_playful_music(self) -> None:
        self.assertEqual(
            pipeline.soundtrack_profile("comic"),
            "playful_clown_instrumental_v1",
        )

    def test_heavy_and_unknown_moods_select_weighty_music(self) -> None:
        self.assertEqual(
            pipeline.soundtrack_profile("heavy"),
            "weighty_clown_instrumental_v1",
        )
        self.assertEqual(
            pipeline.soundtrack_profile("unexpected"),
            "weighty_clown_instrumental_v1",
        )

    def test_generation_prompt_requires_original_clown_and_mood(self) -> None:
        paths = pipeline.run_paths("test")
        paths["growth_experiment"] = {}
        prompt = pipeline.build_codex_prompt("test", paths, "life_dialogue")
        self.assertIn('"mood": "<comic or heavy>"', prompt)
        self.assertIn("not a copyrighted movie character", prompt)
        self.assertIn("juliana551107", prompt)

    def test_capacity_failures_are_retryable(self) -> None:
        self.assertTrue(
            pipeline.is_transient_codex_failure(
                "ERROR: Selected model is at capacity. Please try a different model."
            )
        )
        self.assertTrue(pipeline.is_transient_codex_failure("HTTP 429: Too Many Requests"))

    def test_real_generation_errors_are_not_retried(self) -> None:
        self.assertFalse(
            pipeline.is_transient_codex_failure("Main character reference not found")
        )

    def test_codex_capacity_error_retries_and_preserves_attempt_logs(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            paths = {"run_dir": Path(directory), "reference_images": ()}
            results = [
                pipeline.subprocess.CompletedProcess(
                    args=["codex"],
                    returncode=1,
                    stdout="Selected model is at capacity.",
                ),
                pipeline.subprocess.CompletedProcess(
                    args=["codex"],
                    returncode=0,
                    stdout="generation complete",
                ),
            ]
            with (
                mock.patch.object(pipeline, "build_codex_prompt", return_value="prompt"),
                mock.patch.object(pipeline, "CODEX_TRANSIENT_ATTEMPTS", 3),
                mock.patch.object(pipeline, "CODEX_TRANSIENT_RETRY_SECONDS", 1),
                mock.patch.object(pipeline.subprocess, "run", side_effect=results) as run_mock,
                mock.patch.object(pipeline.time, "sleep") as sleep_mock,
                mock.patch.object(pipeline, "log"),
            ):
                pipeline.trigger_codex("test", paths, "life_dialogue", False)

            self.assertEqual(run_mock.call_count, 2)
            sleep_mock.assert_called_once_with(1)
            attempt_log = (paths["run_dir"] / "codex_exec.log").read_text(encoding="utf-8")
            self.assertIn("attempt 1/3 exit=1", attempt_log)
            self.assertIn("attempt 2/3 exit=0", attempt_log)


if __name__ == "__main__":
    unittest.main()
