# Entry for make.fun's ai-judge-relax-01: writes one short, quiet text to a file.

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

TEXT = "\n".join(
    [
        "The iron rests on its heel, warm, while she shakes out the shirt and lays it flat.",
        "One sleeve at a time: she draws the cuff straight and smooths the seam with her palm.",
        "Steam rises when the iron goes down, a small cloud that thins and is gone.",
        "Along the placket she moves an inch at a time, and the wrinkles give up without a sound.",
        "The cotton smells faintly of warmth and clean water.",
        "At the collar she turns the shirt over, unhurried, and does the other side the same.",
        "Finished, it hangs from the chair back, smooth and ordinary, cooling in the still room.",
    ])

with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(TEXT.encode("utf-8"))
