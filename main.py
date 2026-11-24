"""Two Lines to Your Past Self — make.fun entry.

Writes a two-line warning to /output/entry.txt:
line 1 warns the past self about one specific moment,
line 2 says why that moment mattered.
"""

import os

ENTRY_TEXT = (
    "Don't take the night shift on 14 March \u2014 you will fall asleep "
    "at the wheel on the drive home.\n"
    "The crash cost you the car, the job, and a year of walking, "
    "all for one extra paycheck.\n"
)


def validated_text() -> str:
    """Check the entry against the sealed gate before writing it.

    Gate: UTF-8 text, 1 to 280 characters, exactly two lines,
    not only whitespace.
    """
    text = ENTRY_TEXT
    text.encode("utf-8")  # raises if not valid UTF-8-encodable
    if not 1 <= len(text) <= 280:
        raise ValueError(f"entry is {len(text)} chars, must be 1-280")
    lines = text.rstrip("\n").split("\n")
    if len(lines) != 2:
        raise ValueError(f"entry has {len(lines)} lines, must be exactly 2")
    if not text.strip():
        raise ValueError("entry is only whitespace")
    return text


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = validated_text().encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    # Read back to prove the bytes on disk are exactly what was validated.
    with open(path, "rb") as f:
        if f.read() != data:
            raise IOError("entry.txt bytes differ from validated text")


if __name__ == "__main__":
    main()
