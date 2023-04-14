import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller

### Run webrowser
chromedriver_autoinstaller.install()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

browser1 = webdriver.Chrome(options=chrome_options)
browser2 = webdriver.Chrome(options=chrome_options)
###


browser1.get("https://techstepacademy.com/training-ground")

browser1.execute_script(
    'window.open("http://techstepacademy.com/training-ground","_blank");'
)
browser1.execute_script(
    'window.open("http://techstepacademy.com/training-ground","_blank");'
)


# valdyti tab'us    >>>>   ... .window_handles
# browser1.window_handles >> susitrumpinam i tabs
tabs = browser1.window_handles
browser1.switch_to.window(tabs[1])  # 2 tab'as


time.sleep(5)
