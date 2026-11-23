# Devpost submission draft — WordVault (Reddit's Game of the Day Hackathon)

## Project name
**WordVault — Daily Word Puzzle**

## Tagline
One word a day. Everyone plays the same puzzle. Six guesses to crack the vault.

## Description

WordVault is a daily 5-letter word puzzle built for Reddit. Every day at midnight
UTC a new word drops — the same word for every player, everywhere. You get 6
guesses. Green means the letter is right and in the right spot, yellow means it's
in the word but misplaced, grey means it's not there at all.

Why it's made for Reddit:

- **A daily ritual, not a time sink.** One puzzle a day keeps players coming back
  tomorrow — and the "got it in 3!" comments write themselves.
- **Same puzzle, shared conversation.** Because everyone gets the same word, the
  comments section becomes the game: streaks, near-misses, and spoiler-free
  emoji-grid results.
- **Zero friction.** No account, no login, no install, no ads, no tracking. It
  opens instantly inside an Interactive Post and just works — on desktop and
  on mobile.
- **Built to be shared.** One tap copies your result as coloured squares, so
  you can brag without spoiling the word.
- **Practice mode.** Want more? Play a random word any time — your daily
  streak stays untouched.

WordVault is fully client-side (a single HTML file, no backend, no paid APIs),
so it loads fast, costs nothing to run, and never goes down. Stats, streaks and
guess distribution are saved on the player's own device.

Built with plain HTML, CSS and JavaScript on the Devvit Web platform.

## Inspiration
The daily-puzzle ritual — one shared puzzle a day that a whole community solves
together — reimagined as a Reddit-native game where the comments are part of
the fun.

## What it does
- Daily seeded puzzle: same 5-letter word for every player, new at midnight UTC
- 6 guesses with green / yellow / grey tile feedback and flip animations
- On-screen keyboard that tracks letter states
- Streaks, win %, games played, guess-distribution chart (localStorage)
- One-tap spoiler-free share (emoji grid)
- Countdown to the next puzzle
- Practice mode with random words (doesn't affect daily stats)
- Mobile-friendly, works offline after first load

## How I built it
Plain HTML/CSS/JavaScript in a single file — no framework, no build step, no
server. The daily word is picked deterministically from the UTC date
(`ANSWERS[daysSince(11 Nov 2026) % listLength]`), so every player gets the same
word with zero backend. Packaged as a Devvit Web app (Interactive Post).

## Challenges
- Making duplicate-letter scoring correct (e.g. guessing a letter twice when the
  answer has it once) — solved with a two-pass count-based scorer.
- Keeping the whole game in one dependency-free file so it loads instantly
  inside Reddit and costs $0 to host.
- Designing for a 320px phone screen without losing the desktop feel.

## Accomplishments
- A complete, polished, genuinely fun daily game — start screen, game loop,
  win/lose states, stats, sharing, daily reset — in ~50 KB.
- Verified end-to-end in a real browser: full winning game, mid-game state,
  stats persistence, no console errors, no network requests.

## What's next
- Reddit-native leaderboards via Devvit Redis (daily streak leaderboard per subreddit)
- A "hard mode" (revealed hints must be reused)
- Community word suggestions voted on by players

## Built with
HTML, CSS, JavaScript, Devvit Web (Reddit Developer Platform)

## Links (fill in after publishing)
- App listing: https://developers.reddit.com/apps/wordvault (TODO — user step)
- GitHub repo: https://github.com/kuro1996/wordvault (TODO — user step)
- Demo video: (optional, 2 min max — record a playthrough of ?demo=win)
