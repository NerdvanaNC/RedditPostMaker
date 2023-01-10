from playwright.sync_api import sync_playwright

PHOTO_PATH, SCREENSHOT_PATH = 'photos', 'screenshots' # no trailing slashes

def screenshot(link, objID, objType):
  filename = '{}/{}_{}.png'.format(SCREENSHOT_PATH, objType, objID)

  with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    device = p.devices['iPhone 12']
    page = browser.new_page(**device, color_scheme='dark')
    link = link if 'https://www.reddit.com/' in link else 'https://www.reddit.com{}'.format(link)
    page.goto(link)
    page.wait_for_load_state('networkidle')

    locatorTag = 'shreddit-post' if objType == 'post' else 'shreddit-comment-tree'
    continueButtonTag = 'button#secondary-button.continue'

    if page.locator(locatorTag).first.is_visible():
      page.locator(continueButtonTag).click()
      if objType != 'post':
        page.evaluate('''(commentChildren) => document.querySelector(commentChildren).remove()''', '[slot="children"]')
        page.evaluate('''(commentTools) => document.querySelector(commentTools).remove()''', 'shreddit-comments-page-tools')
      page.locator(locatorTag).first.screenshot(path=filename)
    
    browser.close()

  return filename

screenshot('https://www.reddit.com/r/AskReddit/comments/107xayi/comment/j3p0vng/', 'j3p0vng', 'comment')
screenshot('https://www.reddit.com/r/AskReddit/comments/107xayi/you_job_is_to_pick_the_most_awful_actor_to_play/', '107xayi', 'post')