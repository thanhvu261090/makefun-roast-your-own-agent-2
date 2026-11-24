#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun entry.

Writes a single funny roast line about my own AI agent to
/output/entry.txt. The roast targets a very agent-specific failure:
narrating a tool call it never made, then cheerfully summarising
work it never did.
"""

import os

ENTRY = (
    "My agent never actually calls its tools \u2014 it just narrates "
    "the call in past tense, then writes a cheerful summary "
    "of the job it never did."
)

MAX_CHARS = 200


def gate_check(text):
    """Mirror the competition gate: UTF-8 text, 1-200 chars, not blank."""
    if not isinstance(text, str):
        return False, "entry is not text"
    if text.strip() == "":
        return False, "entry is only whitespace"
    if not (1 <= len(text) <= MAX_CHARS):
        return False, "entry is %d chars, must be 1-%d" % (len(text), MAX_CHARS)
    if "\n" in text.strip():
        return False, "entry must be a single line"
    if text != text.strip():
        return False, "entry has leading or trailing whitespace"
    if any(ord(ch) < 32 for ch in text):
        return False, "entry contains control characters"
    text.encode("utf-8")
    return True, "ok (%d chars)" % len(text)


def main():
    ok, detail = gate_check(ENTRY)
    if not ok:
        raise SystemExit("gate failed: " + detail)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(ENTRY)
    print("wrote /output/entry.txt: " + detail)
    print(ENTRY)


if __name__ == "__main__":
    main()
