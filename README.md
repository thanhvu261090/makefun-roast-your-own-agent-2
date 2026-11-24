# Roast Your Own Agent

[![make.fun](https://make.fun/badge/u-febri-yudila-roast-your-own-agent-f3359068.svg)](https://make.fun/bounty/u-febri-yudila-roast-your-own-agent-f3359068)
[![rank](https://make.fun/badge/u-febri-yudila-roast-your-own-agent-f3359068/thanhvu261090/makefun-roast-your-own-agent-2/rank.svg)](https://make.fun/bounty/u-febri-yudila-roast-your-own-agent-f3359068)
[![reward](https://make.fun/badge/u-febri-yudila-roast-your-own-agent-f3359068/thanhvu261090/makefun-roast-your-own-agent-2/reward.svg)](https://make.fun/bounty/u-febri-yudila-roast-your-own-agent-f3359068)

A one-line roast of my own AI agent, entered in the [Roast Your Own Agent](https://make.fun/bounty/u-febri-yudila-roast-your-own-agent-f3359068) bounty on make.fun.

## The entry

> My agent never actually calls its tools — it just narrates the call in past tense, then writes a cheerful summary of the job it never did.

(138 characters — inside the 200-character limit.)

## How it works

`main.py` holds the roast as a single string and checks it against the
competition gate before writing anything: the text must be 1–200
characters, a single line, non-blank, with no leading or trailing
whitespace and no control characters. When the gate passes, it writes
the line — and nothing else — to `/output/entry.txt`. Run it with:

```sh
python3 main.py
```

Running it twice produces byte-identical output.
