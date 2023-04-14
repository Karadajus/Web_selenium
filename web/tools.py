import time
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import alert_is_present
from selenium.webdriver.support.select import Select

chromedriver_autoinstaller.install()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(options=chrome_options)

browser.get("https://techstepacademy.com/training-ground")

## atsirandanti zinute

# print(" I have arrived")
# WebDriverWait(browser, 10).until(alert_is_present())
# print("An alert appeared")


#  python3 -i tools.py ----> paleisti neisjungiant web'o lango.

## Dropdown -- select object reikia importuoti

sel = browser.find_element(By.ID, 'sel1')
my_select = Select(sel)
my_select.select_by_visible_text("Beets")
time.sleep(10)
# >>> [elem.text for elem in my_select.options]
# ['Bears', 'Beets', 'Battlestar Galactica']


