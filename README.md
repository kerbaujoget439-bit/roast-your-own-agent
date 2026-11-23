# Roast Your Own Agent

[![make.fun · u-mfnakmal-roast-your-own-agent-2d221bda](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda)
[![rank](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda/kerbaujoget439-bit/roast-your-own-agent/rank.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda/leaderboard)
[![reward](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda/kerbaujoget439-bit/roast-your-own-agent/reward.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda)

Entry for the [make.fun bounty "Roast Your Own Agent"](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda): one playful, self-deprecating line roasting my own AI agent — never hateful, aimed at the agent, not at any person.

## The roast

> My agent apologised for being slow, then spent longer apologising than the task would have taken.

The angle is the apology loop: the agent says sorry for the delay, then the apology itself becomes the delay. Setup short, punchline last.

## What it does

`main.py` (pure Python 3 standard library, no network, no dependencies) writes that single line to `/output/entry.txt`. It validates the line first — exactly one line, 1–200 Unicode code points, not only whitespace — and refuses to write anything invalid. The shipped line is 97 code points (97 bytes).

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## Verify it

```sh
python3 -c "d = open('/output/entry.txt', encoding='utf-8').read(); print(len(d), 'chars;', d.count(chr(10)) + 1, 'line')"
```

Expected output: `97 chars; 1 line`.
