"""One Cloud, a Million Litres.

The entry compares rain to a gardener tipping an oversized watering can
across a whole street: the falling water and the even spread match, but the
scale does not. A household can carries about two litres; a single storm
cloud can release around a million litres over one street.

Running this script writes the two-line entry to ``entry.txt`` inside the
output directory (``/output`` by default, or ``$OUTPUT_DIR`` when set).
"""

import os

LINE_1 = (
    "Rain is the sky tipping one giant watering can over the whole street, "
    "so every roof, leaf, and parked bike gets the same drink at once."
)

LINE_2 = (
    "It maps the falling water and the even spread, but leaves out the "
    "scale \u2014 a real can holds two litres, while one storm cloud can "
    "drop a million litres on a single street."
)

ENTRY = LINE_1 + "\n" + LINE_2


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    # No trailing newline: the gate counts every character, so the file
    # must end exactly at the final full stop of line 2.
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
