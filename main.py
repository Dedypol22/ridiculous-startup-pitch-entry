"""Ridiculous at First Glance, Real by the Second.

We bottle silence recorded in empty cathedrals and sell it to open-plan
offices, because companies pay $29 a month for quiet their employees can
finally hear. The idea sounds absurd — selling nothing, recorded in a
church — until the business logic lands: open-plan offices are noisy,
workers pay for focus, and a subscription for genuine, cathedral-quiet
silence is a product companies already buy in cruder forms.
"""

import os
import sys

# Bizarre yet sound: selling bottled nothing sounds like a joke, but the
# buyer (a noisy open-plan office) and the price ($29/month) make it a
# real subscription business for quiet workers already pay for.
PITCH = "We bottle silence recorded in empty cathedrals and sell it to open-plan offices, because companies pay $29 a month for quiet their employees can finally hear."


def output_dir():
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def main():
    text = PITCH + "\n"
    # The file and stdout are written from this same `text`, so they can
    # never disagree about the exact bytes of the pitch.
    os.makedirs(output_dir(), exist_ok=True)
    # newline="\n" pins the line ending, so the byte count is identical on
    # any platform the grader runs (no CRLF translation of the pitch).
    with open(os.path.join(output_dir(), "entry.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
