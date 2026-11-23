# Devvit packaging notes — WordVault → developers.reddit.com → Devpost

Goal: turn the local build (`index.html`) into a Devvit Web app with an app
listing on developers.reddit.com, then link that listing in the Devpost
submission. **All steps below are user-only** (they need the user's Reddit
account / Reddit login). Nothing here has been done yet.

## Prerequisites (user)

1. A Reddit account (the one that will own the app).
2. Node.js 20+ and npm (already on this VM: Node v24).
3. A GitHub repo for the project (optional but recommended for the Devpost
   submission; public repo, e.g. `kuro1996/wordvault`).

## 1. Install the Devvit CLI

```bash
npm install -g devvit
devvit --version
```

Docs: https://developers.reddit.com/docs

## 2. Log in (user step — needs Reddit login in the browser/terminal)

```bash
devvit login
```

This opens a Reddit OAuth flow. Log in with the Reddit account that will own
the app. The CLI stores a token locally — never share it.

## 3. Create the Devvit Web app

```bash
mkdir wordvault-devvit && cd wordvault-devvit
devvit new --template web   # choose the "web" (Devvit Web) template
```

This creates a project with (typical layout):

```
wordvault-devvit/
  package.json
  devvit.json          # app config: name, description, permissions
  src/
    server/            # optional server entry (we don't need one)
  webroot/             # <-- static web app served in the post
    index.html
```

## 4. Drop the game in

```bash
cp ~/workspace/devpost5/reddit-daily-game/index.html webroot/index.html
```

No changes needed: the game is a single self-contained file, no build step,
no external requests. (If the template's `webroot/` has its own starter
`index.html`, replace it.)

Check `devvit.json`:
- `name`: `wordvault` (must be unique; if taken, pick e.g. `wordvault-daily`)
- `description`: one line, e.g. "A daily 5-letter word puzzle — one word a day, same for everyone."
- No special permissions needed (no Reddit API reads, no Redis for v1).

## 5. Test locally in the Devvit playground

```bash
devvit playtest
```

This opens a test subreddit where you can create a post with the app and play
it end-to-end. Verify: board renders, keyboard works, a full game completes,
stats persist, share copies the emoji grid.

## 6. Publish (create the app listing)

```bash
devvit upload    # uploads the build
devvit publish   # publishes a version
```

Then in the Reddit Developer Portal (https://developers.reddit.com):
- Open the app → the listing page URL looks like
  `https://developers.reddit.com/apps/wordvault`
- The app **does NOT need to be installed in a public subreddit to qualify**
  for the hackathon — it can remain private/unlisted. The listing link is
  what the Devpost submission needs.

## 7. Submit on Devpost (user step — needs Devpost login)

1. Go to https://redditgameofday2026.devpost.com/ → "Submit a project"
   (deadline: **8 Dec 2026 21:00 ET = 9 Dec 2026 09:00 WIB**).
2. Paste the description from `DEVPOST_DRAFT.md`.
3. Paste the app listing link from step 6 as the project link.
4. Upload 2–4 screenshots from `screenshots/` (≤256 KiB each).
5. Add the GitHub repo link if created.
6. Submit. Devpost shows a project ID + public page URL — that is the proof
   of submission.

## Optional upgrades (after v1 is submitted)

- **Leaderboards:** add Devvit Redis + a tiny server endpoint to store daily
  scores per subreddit (needs `src/server/` + Redis permission in `devvit.json`).
- **Install in a test subreddit** you moderate, so judges can play it live
  in a real post.
- **Demo video (≤2 min):** screen-record a playthrough of
  `index.html?demo=win` with the stats modal + share step.

## Cost check

- Devvit CLI / developer account: free.
- Hosting the web app: free (Devvit Web hosting).
- Devpost entry: free. **Total: $0.**
