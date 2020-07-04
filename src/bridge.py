import time
from selenium import webdriver


options = webdriver.ChromeOptions()
#options.add_argument("headless")

driver = webdriver.Chrome(options=options)

def read_story(driver: webdriver.Chrome) -> str:
    # Wait for the DOM element containing the story to appear.
    # This is useful when first entering the game, mostly.
    while True:
        try:        
            story_element = driver.find_element_by_css_selector("span[typinganimationduration]")
            break
        except:
            pass

    # Determine the frequency at which we should poll the story for cessation of updates.
    # This is to get around the typewriter animation effect.
    poll_frequency = float(story_element.get_attribute("typinganimationduration")) / 1000

    # Store the initial story so that we can wait until it actually changes.
    # This allows us to get around "thinking" time by the AI, as well as DOM update delays
    # due to rendering or Javascript.
    story = story_element.text
    initial_len = len(story)

    while len(story_element.text) == initial_len:
        pass

    while True:
        time.sleep(poll_frequency)
        prev_len = len(story)
        try:
            story = story_element.text
            # If the story hasn't changed since the last poll, it's done being typed.
            if len(story) == prev_len:
                return story
        except:
            continue

def send_command(driver: webdriver.Chrome, command: str):
    # Type command into textbox.
    driver.find_element_by_css_selector("textarea").send_keys(command)
    # Submit command.
    driver.find_element_by_css_selector("div[aria-label='Submit']").click()

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
    
    print(read_story(driver)) # Read setting selection menu.
    send_command(driver, "1")
    print(read_story(driver)) # Read character selection menu.
finally:
    try:
        driver.close()
    except:
        pass
