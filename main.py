# ai-judge-relax-01 entry (Python 3.13, standard library only).
# Writes one fixed text to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt
# outside the grader). No network; the same bytes on every run.

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

TEXT = "\n".join(
    [
        "The watering can is tin, dented on one side, and it pours in a thin, bright thread.",
        "She waters the mint first, then the basil, then the small pot with no name.",
        "Between each pot she waits. The soil darkens as it drinks, slowly, from the edges in.",
        "On a mint leaf one drop sits, round and whole, in no rush to fall.",
        "The can gets lighter. Her arm notices before she does.",
        "Nothing here is being hurried into growing; the green just stands, wet and ordinary and enough.",
        "She sets the empty can back on the sill, in its ring of rust, where tomorrow will find it.",
    ]
)

with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(TEXT.encode("utf-8"))
