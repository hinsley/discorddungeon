from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_argument("headless")
options.add_argument('window-size=1200x600')

driver = webdriver.Chrome(chrome_options=options)

try:
    driver.get(r"https://play.aidungeon.io/")

    print(driver.find_element_by_css_selector("body").text)
finally:
    try:
        driver.close()
    except:
        pass
