from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

PATH = "/usr/bin/chromedriver"
driver = webdriver.Chrome(options=options, executable_path=PATH)

driver.get("https://monkeytype.com/")
config = driver.find_element(By.ID, "testConfig")
time1 = config.find_element(By.CLASS_NAME, "time")
times = time1.find_elements(By.CLASS_NAME, "textButton")
fifteen = times[0]
fifteen.click()

time_wrapper = driver.find_element(By.ID, "miniTimerAndLiveWpm")
time_left = time_wrapper.find_element(By.CLASS_NAME, "time")

wrapper = driver.find_element(By.ID, "words")
t_end = time.time() + 15
while time.time() < t_end:
    current_word = wrapper.find_element(By.CLASS_NAME, "active")
    driver.find_element(By.ID, "wordsInput").send_keys(current_word.text + " ")
