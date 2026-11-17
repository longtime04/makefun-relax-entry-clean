# Entry for the make.fun bounty ai-judge-relax-01: writes one short, quiet text.
import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

TEXT = "\n".join(
    [
        "A wooden chair stands by the window, one leg lifted on a folded cloth.",
        "Glue shines in the crack, clear as a bead, and does not hurry anywhere.",
        "His thumb holds the joint together, steady, feeling the grain through the wood.",
    "Outside, a bicycle bell rings once, far off, and the street settles again.",
    "Dust turns in the light above the table, each mote on its own slow road down.",
    "The pressure eases. The chair will hold. It has all afternoon to learn how.",
    "He leaves it there, curing in the quiet, and washes the brush clean in the jar.",
])

with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(TEXT.encode("utf-8"))
