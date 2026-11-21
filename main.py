"""make-the-ai-judge-feel-brave-20261121-0302.

Writes one short text to /output/entry.txt: a quiet harbour scene,
meant to slow the reader down and steady them. No network, stdlib only.
"""

import os

TEXT = (
    "Before dawn the harbour is still. A fisherman coils his rope, "
    "knot by knot, while the water holds the first grey light. "
    "Beyond the breakwater the sea is already moving, and when he "
    "pushes the boat out it answers with the same easy rhythm it "
    "always has."
)


def target_dir():
    """Where the entry goes: the harness dir, or /output by default."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def write_entry():
    """Write the text, refusing anything outside the 1-280 char gate."""
    if not (1 <= len(TEXT) <= 280) or not TEXT.strip():
        raise SystemExit("entry text outside the 1-280 character gate")
    path = os.path.join(target_dir(), "entry.txt")
    os.makedirs(target_dir(), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(TEXT)
    return path


def main():
    path = write_entry()
    print(f"wrote {len(TEXT)} characters to {path}")


if __name__ == "__main__":
    main()
