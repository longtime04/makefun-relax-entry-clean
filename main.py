# ai-judge-relax-01 entry (Python 3.13, standard library only).
# Writes one fixed text to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt
# outside the grader). The program runs twice with no network and both runs
# must write the same bytes, so the text is a constant, written in bytes mode
# to keep the exact line ends below.

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

TEXT = "\n".join(
    [
        "The rain has finished, and it is not coming back today.",
        "Under the eaves, the barrel takes a drip, waits, takes another; the sound is small and in no hurry.",
        "The tools are wiped and hung in their outlines.",
        "The kettle, off the heat, ticks twice as it cools, then forgets to.",
        "Nothing in the yard is drying, ripening, or waiting to be carried anywhere.",
        "Light leans in through the high window and lies down in the sawdust.",
        "A sparrow lands on the sill, looks at the quiet, and stays a while.",
        "On the bench, the mug has gone lukewarm, and it can stay lukewarm.",
        "Beyond the gate the lane runs empty to the hill, and the hill is doing nothing at all, slowly, all the way down to evening.",
    ]
)

with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(TEXT.encode("utf-8"))
