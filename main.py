# Entry program for the make.fun ai-judge-relax-01 bounty.
import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

TEXT = """The gutter above the porch has been dripping all afternoon, meltwater off the roof, quick and bright in the sun.

By six the light is going and the drops have slowed. One falls, and rings the bucket below. A long while. Then another, softer, as if the bucket were further away.

The cold comes back the way it left, without asking. A skin of ice spreads over the puddle by the step, from the edges in.

Now a drop gathers at the lip of the gutter, swells, and hangs. It catches the last of the light and holds it. It does not fall.

Another is forming behind it, slower still.

The house is dark except for one window, and nobody is waiting for the bucket to fill. The roof has all night to give up its water, and the cold has all night to take it, one held drop at a time."""

with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(TEXT.encode("utf-8"))
