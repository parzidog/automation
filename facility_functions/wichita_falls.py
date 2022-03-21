import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome('../chromedriver')

driver.get("https://www.webselfstorage.com/SignIn")
driver.maximize_window()

driver.implicitly_wait(4)

username = driver.find_element(By.XPATH, '//*[@id="userName"]')
username.click()
#Enter new username
#text = "kenneth_wf"   
for character in text:
    username.send_keys(character)
    time.sleep(0.1) # pause for 0.3 seconds("kenneth_wf")

driver.implicitly_wait(1)

password = driver.find_element(By.XPATH, '//*[@id="Password"]')
password.click()
text = "Storage1!"
for character in text:
    password.send_keys(character)
    time.sleep(0.1) # pause for 0.3 seconds

driver.implicitly_wait(1)

signIn = driver.find_element(By.XPATH, '//*[@id="login_form"]/div/div[4]/input')
signIn.click()

driver.implicitly_wait(1)

reports = driver.find_element(By.XPATH, '//*[@id="ctReports"]')
reports.click()

driver.implicitly_wait(1)

#Collection Worksheet

collectionWorksheet = driver.find_element(By.XPATH, '//*[@id="reportsListWidget"]/div/div[1]/div/ul/li[4]/a')
ActionChains(driver) \
    .key_down(Keys.CONTROL) \
    .key_down(Keys.SHIFT) \
    .click(collectionWorksheet) \
    .key_up(Keys.CONTROL) \
    .key_up(Keys.SHIFT) \
    .perform()

driver.switch_to.window(driver.window_handles[1])

fromDays = driver.find_element(By.XPATH, '//*[@id="ReportArguments_FromDaysLate"]')
fromDays.click()
fromDays.clear()
fromDays.send_keys("1")

fromDays = driver.find_element(By.XPATH, '//*[@id="ReportArguments_ToDaysLate"]')
fromDays.click()
fromDays.clear()
fromDays.send_keys("999")
fromDays.send_keys(Keys.ENTER)

driver.switch_to.window(driver.window_handles[-1])
