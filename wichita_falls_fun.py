import time
import os
import platform
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

op_sys = platform.system()

if op_sys == 'Darwin':
    s=Service(executable_path='/Users/parzidog/Documents/GitHub/automation/chromedriver.exe')
    driver = webdriver.Safari()

elif op_sys == 'Windows':
    os.system('set PATH=%PATH%;D:\chromedriver.exe')
    s = Service(executable_path='/Users/WichitaFalls/Documents/automation/chromedriver.exe')
    driver = webdriver.Chrome(service=s)

else:
    print('System is not compatible or something went wrong\. Ask Kenny for help!')

driver.get("https://www.webselfstorage.com/SignIn")
driver.minimize_window()

driver.headless = True

driver.implicitly_wait(4)

username = driver.find_element(By.XPATH, '//*[@id="userName"]')
username.click()
#Enter new username
text = "kenneth_wf"
for character in text:
    username.send_keys(character)
    time.sleep(0.1)  # pause for 0.3 seconds("kenneth_wf")

driver.implicitly_wait(1)

password = driver.find_element(By.XPATH, '//*[@id="Password"]')
password.click()
#Enter new password
text = "Storage1!"
for character in text:
    password.send_keys(character)
    time.sleep(0.1)  # pause for 0.3 seconds

driver.implicitly_wait(1)

signIn = driver.find_element(
    By.XPATH, '//*[@id="login_form"]/div/div[4]/input')
signIn.click()

driver.implicitly_wait(1)

reports = driver.find_element(By.XPATH, '//*[@id="ctReports"]')
reports.click()

driver.implicitly_wait(1)

#Collection Worksheet

collectionWorksheet = driver.find_element(
    By.XPATH, '//*[@id="reportsListWidget"]/div/div[1]/div/ul/li[4]/a')
ActionChains(driver) \
    .key_down(Keys.CONTROL) \
    .key_down(Keys.SHIFT) \
    .click(collectionWorksheet) \
    .key_up(Keys.CONTROL) \
    .key_up(Keys.SHIFT) \
    .perform()

driver.implicitly_wait(1)
driver.switch_to.window(driver.window_handles[1])
driver.implicitly_wait(2)

fromDays = driver.find_element(
    By.XPATH, '//*[@id="ReportArguments_FromDaysLate"]')
fromDays.click()
fromDays.clear()
fromDays.send_keys("1")
driver.implicitly_wait(1)

fromDays = driver.find_element(
    By.XPATH, '//*[@id="ReportArguments_ToDaysLate"]')
fromDays.click()
fromDays.clear()
fromDays.send_keys("999")
fromDays.send_keys(Keys.ENTER)

driver.implicitly_wait(2)

driver.switch_to.window(driver.window_handles[0])

#Occupancy Rate Exceptions

driver.implicitly_wait(1)

RateExceptions = driver.find_element(
    By.XPATH, '//*[@id="reportsListWidget"]/div/div[2]/div[3]/ul/li[1]/a')
ActionChains(driver) \
    .key_down(Keys.CONTROL) \
    .key_down(Keys.SHIFT) \
    .click(RateExceptions) \
    .key_up(Keys.CONTROL) \
    .key_up(Keys.SHIFT) \
    .perform()

driver.implicitly_wait(1)

driver.switch_to.window(driver.window_handles[2])

driver.implicitly_wait(1)

# printRateExceptions = driver.find_element(By.XPATH, '//*[@id="printReport"]')
# printRateExceptions.click()

driver.implicitly_wait(1)

driver.switch_to.window(driver.window_handles[0])

#Management Summary

driver.implicitly_wait(2)

managementSummary = driver.find_element(
    By.XPATH, '//*[@id="reportsListWidget"]/div/div[3]/div[2]/ul/li[8]/a')
ActionChains(driver) \
    .key_down(Keys.CONTROL) \
    .key_down(Keys.SHIFT) \
    .click(managementSummary) \
    .key_up(Keys.CONTROL) \
    .key_up(Keys.SHIFT) \
    .perform()

driver.implicitly_wait(1)


driver.switch_to.window(driver.window_handles[3])

driver.implicitly_wait(1)

printManagementSummary = driver.find_element(
    By.XPATH, '//*[@id="iframeContents"]/div/section/div/form/div[2]/div[2]/button')
printManagementSummary.click()

driver.implicitly_wait(1)

driver.switch_to.window(driver.window_handles[0])

driver.implicitly_wait(2)

#Occupancy Overview

occupancyOverview = driver.find_element(
    By.XPATH, '//*[@id="reportsListWidget"]/div/div[3]/div[2]/ul/li[11]/a')
ActionChains(driver) \
    .key_down(Keys.CONTROL) \
    .key_down(Keys.SHIFT) \
    .click(occupancyOverview) \
    .key_up(Keys.CONTROL) \
    .key_up(Keys.SHIFT) \
    .perform()

driver.switch_to.window(driver.window_handles[4])

# printOccupancyOverview = driver.find_element(
# By.XPATH, '//*[@id="printReport"]')
# fromDays.click()

driver.switch_to.window(driver.window_handles[0])
