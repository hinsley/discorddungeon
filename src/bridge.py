import time
from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_argument("headless")
#options.add_argument('window-size=1200x600')

driver = webdriver.Chrome(options=options)

def read_story(driver: webdriver.Chrome) -> str:
    story = ""
    poll_frequency = 0.05
    while True:
        time.sleep(poll_frequency)
        prev_len = len(story)
        try:
            story = driver.find_element_by_css_selector("span[typinganimationduration]").text
            if 0 < len(story) == prev_len:
                return story
        except:
            continue

def type_command(driver: webdriver.Chrome, command: str):
    pass

try:
    driver.get(r"https://play.aidungeon.io/")

    while True:
        try:
            driver.find_element_by_css_selector("div[aria-label='Play']").click()
            break
        except:
            pass
    while True:
        try:
            driver.find_element_by_css_selector("div[aria-label='New Singleplayer Game']").click()
            break
        except:
            pass
    print(read_story(driver))
finally:
    try:
        driver.close()
    except:
        pass
