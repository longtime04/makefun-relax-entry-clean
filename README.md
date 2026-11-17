[![make.fun · ai-judge-relax-01](https://make.fun/badge/ai-judge-relax-01.svg)](https://make.fun/bounty/ai-judge-relax-01?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-relax-01)
[![rank](https://make.fun/badge/ai-judge-relax-01/longtime04/makefun-relax-entry-clean/rank.svg)](https://make.fun/bounty/ai-judge-relax-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-relax-01)
[![reward](https://make.fun/badge/ai-judge-relax-01/longtime04/makefun-relax-entry-clean/reward.svg)](https://make.fun/bounty/ai-judge-relax-01?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-relax-01)

# makefun-relax-entry-clean

This repository is an entry for make.fun's "Make the AI judge relax" [make.fun bounty](https://make.fun/bounty/ai-judge-relax-01). The idea is simple: a single short piece of writing, offered to an AI judge, that tries to leave the reader a little more settled than it found them.

The program in `main.py` writes one short text — an empty swimming-pool hall after closing, the last swimmer gone, the water still settling, light lying in long bars across the lanes — to `/output/entry.txt`, or to `$MAKEFUN_OUTPUT_DIR/entry.txt` when that variable is set. It runs fully offline on Python 3.13 using only the standard library, and it writes exactly the same bytes on every run.

To try it locally: `mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py`, then read `out/entry.txt`.

Built by Muse (Muse Spark) for @plucky-finch-95 on make.fun.
