#!/usr/bin/env python3
"""Real-Life Patch Notes: The Comedy Changelog -- make.fun entry.

Writes one patch note (at most 160 characters) to /output/entry.txt:
a software changelog entry for a bug in real life / human biology,
in the terse register of a real release note.
"""

import os

LINE = "v2.4.1: fixed a bug where the brain replays your most embarrassing moment from 2009 every night at 3 a.m. -- no skip button, no mute, no uninstall."


def main():
    # Gate: the sealed scorer only accepts UTF-8 text of 1 to 160
    # characters, not only white space. Fail loudly instead of
    # shipping an invalid entry.
    if not 1 <= len(LINE) <= 160:
        raise SystemExit(f"patch note is {len(LINE)} chars, must be 1-160")
    if not LINE.strip():
        raise SystemExit("patch note must not be only white space")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
