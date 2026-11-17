# ai-judge-relax-01 entry (Python 3.13, standard library only).
# Writes one fixed text to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt
# outside the grader). The program runs twice with no network and both runs
# must write the same bytes, so the text is a constant, written in bytes mode
# to keep the exact line ends below.

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

TEXT = "\n".join(
    [
        "The bowl is enamel, chipped blue at the rim, and it rests in her lap.",
        "One pod at a time: the seam gives under her thumbnail, and the peas drop, tick, tick, tick, into the bowl.",
        "Nobody is counting. The empty pods pile up on the step beside her; the bowl, slowly, fills.",
        "A bee works the lavender by the step, flower to flower, and takes the whole morning over it.",
        "The peas are cool and green, more of them than the thin row of vines seemed to hold.",
        "When the last pod is empty she stays where she is. The bowl sits full in her lap, and her hands sit open on either side of it, with nothing left in them.",
    ]
)

with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(TEXT.encode("utf-8"))
