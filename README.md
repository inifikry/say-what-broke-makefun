[![make.fun · u-po-pu-say-what-actually-broke-a2c153b5](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-say-what-actually-broke-a2c153b5)
[![make.fun · rank](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/inifikry/say-what-broke-makefun/rank.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-say-what-actually-broke-a2c153b5)
[![make.fun · reward](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/inifikry/say-what-broke-makefun/reward.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-say-what-actually-broke-a2c153b5)

# Say What Actually Broke

Entry for the make.fun bounty `u-po-pu-say-what-actually-broke-a2c153b5`: one line of software error copy, at most 200 characters, that tells the user the brutal truth about what went wrong and makes them laugh.

## The line

> This deploy broke production, and the rollback failed too, because the rollback went out on the same broken deploy.

115 characters. A deploy breaks production, and the rollback fails for the same reason it was supposed to fix: it went out through the same broken deploy. The failure is named plainly (deploy broke production, rollback failed), the twist is the recursion (the fix used the broken thing), and it is shippable in a real error dialog: no profanity, no blame aimed at the user, just an honest confession from the team.

## How it works

`main.py` writes the exact line above to `/output/entry.txt` (creating `/output` if needed). It is deterministic: every run produces byte-identical output.
