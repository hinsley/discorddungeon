import time
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException


options = webdriver.ChromeOptions()
#options.add_argument("headless")

driver = webdriver.Chrome(options=options)

def get_element(driver: webdriver.Chrome, css_selector: str) -> webdriver.remote.webelement.WebElement:
    while True:
        try:
            return driver.find_element_by_css_selector(css_selector)
        except:
            pass

def read_story(driver: webdriver.Chrome) -> str:
    while True:
        try:
            # Wait for the DOM element containing the story to appear.
            # This is useful when first entering the game, mostly.
            while True:
                try:        
                    story_element = get_element(driver, "span[typinganimationduration]")
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
        except:
            continue

def send_command(driver: webdriver.Chrome, command: str):
    # Type command into textbox.
    get_element(driver, "textarea").send_keys(command)
    # Submit command.
    get_element(driver, "div[aria-label='Submit']").click()

try:
    driver.get(r"https://play.aidungeon.io/")

    get_element(driver, "div[aria-label='Play']").click()
    get_element(driver, "div[aria-label='New Singleplayer Game']").click()
    
    print(read_story(driver)) # Read setting selection menu.
    send_command(driver, "1")
    print(read_story(driver)) # Read character selection menu.
    send_command(driver, "1")
    print(read_story(driver)) # Read character name prompt.
    send_command(driver, "John Hancock")
    print(read_story(driver)) # Read "Generating story...".
    
    # Click off the "New Quest" dialog.
    action = webdriver.common.action_chains.ActionChains(driver)
    action.move_to_element_with_offset(driver.find_element_by_tag_name("body"), 0, 0).click().perform()

    print(read_story(driver))
    input()
finally:
    try:
        driver.close()
    except:
        pass
