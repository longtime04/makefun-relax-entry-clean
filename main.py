# Entry for make.fun ai-judge-relax-01: writes one short text to entry.txt.
import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

TEXT = "\n".join([
    "The last swimmer has gone, and the water is still settling from the day.",
    "The lane ropes drip, slowly, one drop at a time, into the still water.",
    "Light comes through the high windows and lies in long bars across the lanes.",
    "The lifeguard's chair stands empty, a towel hook bare beside it.",
    "A faint smell of chlorine hangs over the water, fading.",
    "Somewhere a pump ticks off, and the hall holds only its own small sounds.",
    "The water is flat now, the light rests where it lies, and the two of them have all night.",
])

with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(TEXT.encode("utf-8"))
