# Entry for make.fun's ai-judge-relax-01 bounty.
# Writes one short, quiet text to entry.txt. No network, no randomness:
# the same bytes come out on every run.

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

TEXT = "\n".join(
    [
        "The needles settle into their rhythm: a soft click, a pause, a soft click.",
        "Against her shoe, the ball of grey yarn gives up its thread a little at a time.",
        "The row lengthens the way grass grows, too slowly to watch, and yet it lengthens.",
        "Below the porch, a screen door sighs shut somewhere and does not slam.",
        "She counts nothing. The stitches keep their own quiet tally, and it is always enough.",
        "Her hands know the pattern the way a river knows its bed, without deciding.",
        "The sweater will be done when it is done; the afternoon is in no hurry, and neither is she.",
    ]
)

with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(TEXT.encode("utf-8"))
