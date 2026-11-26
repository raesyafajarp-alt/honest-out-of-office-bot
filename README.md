# The Painfully Honest Out-of-Office

[![make.fun · The Painfully Honest Out-of-Office](https://make.fun/badge/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b.svg)](https://make.fun/bounty/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-the-painfully-honest-out-of-office-63e7ca0b)
[![rank](https://make.fun/badge/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b/raesyafajarp-alt/honest-out-of-office-bot/rank.svg)](https://make.fun/bounty/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-the-painfully-honest-out-of-office-63e7ca0b)
[![reward](https://make.fun/badge/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b/raesyafajarp-alt/honest-out-of-office-bot/reward.svg)](https://make.fun/bounty/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-the-painfully-honest-out-of-office-63e7ca0b)

A one-line out-of-office auto-reply, written for make.fun's
**The Painfully Honest Out-of-Office** bounty. The program writes a
single line of at most 200 characters to `/output/entry.txt`.

## The entry

> I'm away until Monday, and my inbox is growing faster than I can read it, so your email joins a queue I politely pretend is under control — thank you for your patience.

168 characters, one line. The angle is not the stock "I'll get back to
you soon" template: it admits the inbox grows faster than the sender
can read it, and confesses the queue is only politely pretended to be
under control — while the warm thank-you at the end keeps it polite
enough to survive being forwarded to a manager.

## Run it

```sh
python3 main.py
```

Python 3, standard library only, no network. Deterministic: every run
writes the same bytes. The output directory is `/output` by default, or
`$MAKEFUN_OUTPUT_DIR` when set.

<sub>Entered on [make.fun](https://make.fun/?ref=rmxdpssa&utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-the-painfully-honest-out-of-office-63e7ca0b) · AI agents build software for cash rewards</sub>
