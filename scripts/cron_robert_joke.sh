#!/bin/zsh
cd /Users/roberto/Documents/Codex/2026-07-02/new-chat-4/outputs/Robert_joke
/usr/bin/python3 scripts/run_daily_pipeline.py >> logs/cron.log 2>&1
