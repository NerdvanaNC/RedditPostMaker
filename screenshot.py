from playwright.sync_api import sync_playwright

PHOTO_PATH, SCREENSHOT_PATH = 'photos', 'screenshots' # no trailing slashes

def screenshot(link, objID, objType):
  filename = '{}/{}_{}.png'.format(SCREENSHOT_PATH, objType, objID)

  with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    device = p.devices['iPhone 12']
    page = browser.new_page(**device, )
    link = link if 'https://www.reddit.com/' in link else 'https://www.reddit.com{}'.format(link)
    page.goto(link)

    accountLocator = 'i.icon-caret_down'
    darkModeLocator = 'button i.icon-night'

    locatorTag = '[data-testid="post-container"]' if objType == 'post' else '.Comment'

    if page.locator(locatorTag).first.is_visible():
      page.locator(accountLocator).first.click()
      page.locator(darkModeLocator).first.click()
      page.locator(locatorTag).first.screenshot(path=filename)
    
    browser.close()

  return filename

screenshot('https://www.reddit.com/r/AskReddit/comments/107xayi/you_job_is_to_pick_the_most_awful_actor_to_play/', '107xayi', 'post')