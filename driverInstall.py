import time
import platform

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.safari.service import Service

#CHECK OS FOR SAFARI OR CHROME
op_sys = platform.system()

if(op_sys == 'Darwin'):

    driver = webdriver.Safari()

else:

    driver = webdriver.Chrome('chromedriver')

#LAUNCH AND SIGNIN
driver.get("https://www.webselfstorage.com/SignIn")
driver.maximize_window()

driver.implicitly_wait(6)

username = driver.find_element(By.XPATH, '//*[@id="userName"]')

username.click()

#Enter new username
text = "kenneth_wf"
for character in text:
    username.send_keys(character)
    time.sleep(0.1)  # pause for 0.3 seconds

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

driver.implicitly_wait(10)

reports = driver.find_element(By.XPATH, '//*[@id="ctReports"]')

driver.implicitly_wait(2)

reports.click()

driver.implicitly_wait(5)

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

driver.switch_to.window(driver.window_handles[1])

fromDays = driver.find_element(
    By.XPATH, '//*[@id="ReportArguments_FromDaysLate"]')
fromDays.click()
fromDays.clear()
fromDays.send_keys("1")

fromDays = driver.find_element(
    By.XPATH, '//*[@id="ReportArguments_ToDaysLate"]')
fromDays.click()
fromDays.clear()
fromDays.send_keys("999")
fromDays.send_keys(Keys.ENTER)

driver.switch_to.window(driver.window_handles[-1])

#Occupancy Rate Exceptions

printRateExceptions = driver.find_element(
    By.XPATH, '//*[@id="reportsListWidget"]/div/div[2]/div[3]/ul/li[1]/a')
ActionChains(driver) \
    .key_down(Keys.CONTROL) \
    .key_down(Keys.SHIFT) \
    .click(printRateExceptions) \
    .key_up(Keys.CONTROL) \
    .key_up(Keys.SHIFT) \
    .perform()

driver.switch_to.window(driver.window_handles[1])

printRateExceptions = driver.find_element(By.XPATH, '//*[@id="printReport"]')
printRateExceptions.click()

driver.switch_to.window(driver.window_handles[-1])

#Management Summary

managementSummary = driver.find_element(
    By.XPATH, '//*[@id="reportsListWidget"]/div/div[3]/div[2]/ul/li[8]/a')
ActionChains(driver) \
    .key_down(Keys.CONTROL) \
    .key_down(Keys.SHIFT) \
    .click(managementSummary) \
    .key_up(Keys.CONTROL) \
    .key_up(Keys.SHIFT) \
    .perform()

driver.switch_to.window(driver.window_handles[1])

printManagementSummary = driver.find_element(
    By.XPATH, '//*[@id="iframeContents"]/div/section/div/form/div[2]/div[2]/button')
printManagementSummary.click()

driver.switch_to.window(driver.window_handles[-1])

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

driver.switch_to.window(driver.window_handles[1])

printOccupancyOverview = driver.find_element(
    By.XPATH, '//*[@id="printReport"]')
fromDays.click()

driver.switch_to.window(driver.window_handles[-1])


driver.quit()
