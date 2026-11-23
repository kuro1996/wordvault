# WordVault — Daily Word Puzzle

A polished, original daily word puzzle built for **Reddit's Game of the Day Hackathon**
(Devpost, 11 Nov – 8 Dec 2026, $35,000 in prizes).

Guess the hidden 5-letter word in 6 tries. Everyone gets the **same word every day**
(seeded from the UTC date), so the whole community plays — and argues about —
the same puzzle. Streaks, stats and guess distribution are saved on-device, and
results share as spoiler-free coloured squares.

## Why it's a good daily game

- **One puzzle a day, same for everyone** — the "did you get it in 3?" conversation
  is the whole point of a daily game.
- **Zero friction** — no account, no login, no backend, no tracking, no ads.
  Opens instantly inside a Reddit Interactive Post.
- **Built to be shared** — emoji-grid results are made for comments.
- **Practice mode** — play a random word any time without touching your daily streak.
- **Mobile-first** — on-screen keyboard, touch-friendly, verified at 500px wide (Chrome headless minimum width).

## Tech

- **Plain HTML + CSS + JS, single file** (`index.html`, ~50 KB). No framework,
  no build step, no dependencies, no network calls at runtime.
- **$0 cost** — fully client-side; `localStorage` for state/stats.
- **Devvit Web ready** — the file drops into a Devvit Web app's `webroot/`
  as-is (see `DEVVIT_PACKAGING.md`).

## Run locally

```bash
# any static server works, e.g.:
python3 -m http.server 8000
# then open http://localhost:8000
```

Or just open `index.html` directly in a browser (no server needed).

### Demo states (for screenshots / testing)

- `index.html?demo=playing` — auto-plays two guesses against today's real word.
- `index.html?demo=win` — auto-plays a full winning game (4 guesses).
- `index.html?mode=practice` — practice a random word (stats not counted).

## How the daily word is chosen

`answerFor(date)` = `ANSWERS[daysSince(11 Nov 2026) % ANSWERS.length]`, using the
UTC date. Deterministic, identical for every player, no server needed. The answer
list (566 common 5-letter words) is embedded in the file; the guess list is
answers + 588 extra valid words (593 valid guesses in total).

## Files

| File | What it is |
| --- | --- |
| `index.html` | The whole game (HTML + CSS + JS) |
| `README.md` | This file |
| `DEVPOST_DRAFT.md` | Submission description draft for Devpost |
| `DEVVIT_PACKAGING.md` | Exact steps to package + publish on developers.reddit.com |
| `screenshots/` | Submission screenshots (≤256 KiB each, long side ≤1280) |

## Verification (2026-11-16)

- Loaded in headless Chrome (CDP, `file://`) and played with the real game logic:
  `?demo=win` plays a full 4-guess winning game (CRANE → SLATE → AUDIO →
  ADAPT): tiles flip green/yellow/grey, win modal appears ("You cracked the
  vault in 4/6!"), stats recorded in localStorage (played 1, wins 1,
  streak 1, distribution bar at 4 = 1).
- `?demo=playing` renders a mid-game board (2 guesses scored, keyboard
  states updated, state saved in localStorage).
- No console errors on load or during a full game. No network requests
  (fully self-contained, zero external URLs).
- Mobile layout verified at 390x844: full board + keyboard, no overflow.
- Duplicate-letter scorer unit-checked in Node (APPLE vs PAPER, APPLE vs APPLY).
- Screenshots in `screenshots/` were captured from the real running game
  (1280x663 desktop x3, 500x707 mobile x1; all ≤ 57 KiB).

## License

MIT — free to use, modify and ship.
