"""Record WordVault demo video with Playwright (~42s, under Reddit's 1-min limit)."""
from playwright.sync_api import sync_playwright

URL = "file:///home/hatch/workspace/devpost5/reddit-daily-game/index.html?demo=win"
OUT_DIR = "/home/hatch/workspace/devpost5/reddit-daily-game"

with sync_playwright() as p:
    browser = p.chromium.launch()
    ctx = browser.new_context(
        viewport={"width": 1280, "height": 720},
        record_video_dir=OUT_DIR,
        record_video_size={"width": 1280, "height": 720},
    )
    page = ctx.new_page()
    page.goto(URL)
    page.wait_for_timeout(14000)  # auto-played win: 4 guesses + stats modal opens
    page.click("#shareBtn")
    page.wait_for_timeout(5000)   # share toast
    page.locator('button.close[data-close="statsModal"]').click()
    page.wait_for_timeout(1000)   # close modal
    page.click("#statsBtn")
    page.wait_for_timeout(6000)   # stats modal again
    page.click("#practiceBtn")
    page.wait_for_timeout(9000)   # practice mode board
    page.wait_for_timeout(4000)   # closing shot
    ctx.close()
    browser.close()
print("done")
