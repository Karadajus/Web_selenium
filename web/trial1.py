import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()
chrome_options = webdriver.ChromeOptions()
# Disables the sandbox mode for the browser
chrome_options.add_argument("--no-sandbox")
# Disables hardware acceleration for the browser.
# chrome_options.add_argument("--disable-gpu")
# This option excludes the "enable-logging" switch when starting the Chrome browser
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

browser = webdriver.Chrome(options=chrome_options)

########

browser.get("https://techstepacademy.com/trial-of-the-stones")

## Riddle of stones

stone_input = browser.find_element(By.ID, "r1Input")
stone_answer_button = browser.find_element(By.CSS_SELECTOR, "button#r1Btn")
# pasirodes atsakymas $$("div#passwordBanner > h4")   #-means ID
stone_result = browser.find_element(By.CSS_SELECTOR, "div#passwordBanner > h4")


## Riddle of secrets

# suranda lauka riddle of secrets galima ir "input[id='r2Input']"
secret_input = browser.find_element(By.CSS_SELECTOR, "input#r2Input")
secret_answer_button = browser.find_element(By.CSS_SELECTOR, "button#r2Butn")

## Two mechants
# .text paima texta
richest_mechant_name = browser.find_element(By.XPATH, "//p[text()='3000']/../span").text
mechant_input = browser.find_element(By.ID, "r3Input")
mechant_answer_button = browser.find_element(By.CSS_SELECTOR, "button#r3Butn")
check_button = browser.find_element(By.CSS_SELECTOR, "button#checkButn")
complete_msg = browser.find_element(By.CSS_SELECTOR, "div#trialCompleteBanner h4")

# Run scripts
# time.sleep(10)

stone_input.send_keys("rock")
stone_answer_button.click()
password = stone_result.text

secret_input.send_keys(password)
secret_answer_button.click()

mechant_input.send_keys(richest_mechant_name)
mechant_answer_button.click()
check_button.click()
assert complete_msg.text == "Trial Complete"  # turi gauti tokia reiksme kokia parasyta
time.sleep(10)
