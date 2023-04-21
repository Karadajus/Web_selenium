import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
from base_element import BaseElement  # import from another py file

chromedriver_autoinstaller.install()
chrome_options = webdriver.ChromeOptions()
# Disables the sandbox mode for the browser
chrome_options.add_argument("--no-sandbox")
# Disables hardware acceleration for the browser.
# chrome_options.add_argument("--disable-gpu")
# This option excludes the "enable-logging" switch when starting the Chrome browser
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

browser = webdriver.Chrome(options=chrome_options)


class TrainingGroundPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://techstepacademy.com/training-ground"

    def go(self):
        self.driver.get(self.url)

    @property
    def button1(self):
        locator = (By.ID, "b1")
        return BaseElement(
            driver=self.driver,
            by=locator[0],
            value=locator[1]
        )

    # def type_into_input(self, text):
    #     inpt = self.driver.find_element(By.ID, "ipt1")
    #     inpt.clear()
    #     inpt.send_keys(text)
    #
    # def get_input_text(self):
    #     inpt = self.driver.find_element(By.ID, "ipt1")
    #     elem_text = inpt.get_attribute("value")
    #     print("get_input_text:", elem_text)
    #     return elem_text
    #
    # def click_button_1(self):
    #     self.driver.find_element(By.ID, "b1").click()
    #     # time.sleep(10)
    #     alert = self.driver.switch_to.alert
    #     alert.accept()

# Our test


# Test setup
test_value = "Worked"

# Test
trng_page = TrainingGroundPage(driver=browser)
trng_page.go()
assert trng_page.button1.text == 'Button1'
trng_page.button1.click()
time.sleep(10)

# trng_page.button1.click()
# trng_page.type_into_input(test_value)
# trng_page.click_button_1()
# # time.sleep(10)
# txt_from_input = trng_page.get_input_text()
# assert (
#     txt_from_input == test_value
# ), f"Test Failed: Input did not match expected {test_value}."
# print("Passed")
