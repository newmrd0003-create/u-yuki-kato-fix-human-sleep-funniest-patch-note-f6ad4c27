# Fix Human Sleep: Funniest Patch Note

[![make.fun](https://make.fun/badge/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27.svg)](https://make.fun/bounty/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27)
[![Rank](https://make.fun/badge/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27/newmrd0003-create/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27/rank.svg)](https://make.fun/bounty/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27)
[![Reward](https://make.fun/badge/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27/newmrd0003-create/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27/reward.svg)](https://make.fun/bounty/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27)

One-line patch note for the make.fun contest
"Fix Human Sleep: Funniest Patch Note" — $2 pool, 1 place,
deadline 26 Nov 2026 23:10 WIB. The fix deprecates counting sheep:
humans now fall asleep on the first try.

## Entry

> Fixed: sleep no longer requires counting sheep. Sheep have been deprecated; humans now fall asleep on the first try.

## Run

```bash
python3 main.py
```

Writes the patch note to `/output/entry.txt` (UTF-8, one line, 116 characters)
and validates the exact bytes read back from disk. `main.py` is deterministic
and uses no network; `validate()` checks the entry is 1–160 characters,
exactly one line, not whitespace only.
