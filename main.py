"""Entrypoint: Fix Human Sleep: Funniest Patch Note.

Writes the single-line patch-note entry to /output/entry.txt.
Deterministic: the same bytes on every run.
"""

ENTRY = (
    "Fixed: sleep no longer requires counting sheep. "
    "Sheep have been deprecated; humans now fall asleep on the first try."
)

MAX_CHARS = 160
OUTPUT_PATH = "/output/entry.txt"


def validate(entry: str = ENTRY):
    """Check the entry against the competition gate.

    Gate: UTF-8 text of 1 to 160 characters, not only white space,
    exactly one line.
    Accepts the exact bytes main() writes: a single trailing newline
    is the file terminator, not part of the entry.
    Returns (ok, errors).
    """
    # Strip one trailing newline: the file terminator main() appends.
    if entry.endswith("\n"):
        entry = entry[:-1]
    errors = []
    if not entry or not entry.strip():
        errors.append("entry is empty or only whitespace")
    if len(entry) > MAX_CHARS:
        errors.append(f"entry is {len(entry)} chars, over the {MAX_CHARS} cap")
    if "\n" in entry or "\r" in entry:
        errors.append("entry must be a single line")
    try:
        entry.encode("utf-8")
    except UnicodeEncodeError as exc:
        errors.append(f"entry is not valid UTF-8: {exc}")
    return (len(errors) == 0, errors)


def main():
    ok, errors = validate()
    if not ok:
        raise SystemExit(f"invalid entry: {errors}")
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    # Self-check: re-read what was written and validate the on-disk
    # bytes, so a truncated or corrupted write fails loudly here.
    with open(OUTPUT_PATH, encoding="utf-8", newline="") as f:
        written = f.read()
    ok, errors = validate(written)
    if not ok or written != ENTRY + "\n":
        raise SystemExit(f"write verification failed: {errors}")
    print(f"wrote {OUTPUT_PATH} ({len(ENTRY)} chars)")


if __name__ == "__main__":
    main()
