# Entry for make.fun's ai-judge-relax-01: writes one short, quiet text to a file.

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

TEXT = "\n".join(
    [
        "The water runs cool over the rice, and her hands move slowly through it.",
        "Grains slide from her fingers, white on white, and settle at the bottom again.",
        "She tips the bowl, and the cloudy water leaves in one long, unhurried pour.",
        "Under the tap the grains show clearer this time, like pebbles at the edge of a stream.",
        "Once more her hand goes in; the swirling slows, slows, and the rice comes to rest.",
        "She sets the bowl by the sink, the water over the grains gone still and clear.",
        "The rice soaks. The kitchen keeps its quiet around it, and the light does not change.",
    ])

with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(TEXT.encode("utf-8"))
