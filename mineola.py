import time
import os
import platform
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options


class mineola():
    def getReports():

        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        global browser

        op_sys = platform.system()
        if op_sys == 'Darwin':
            driver = webdriver.Safari()

            def open_tab(driver, report):
                ActionChains(driver) \
                    .key_down(Keys.COMMAND) \
                    .key_down(Keys.SHIFT) \
                    .click(report) \
                    .key_up(Keys.COMMAND) \
                    .key_up(Keys.SHIFT) \
                    .perform()

        elif op_sys == 'Windows':
            os.system('set PATH=%PATH%;D:\chromedriver.exe')
            os.system('set PATH=%PATH%;E:\chromedriver.exe')
            os.system('set PATH=%PATH%F:\chromedriver.exe')
            os.system(
                'set PATH=%PATH%;C:/Users/WichitaFalls/Documents/automation/chromedriver.exe')
            # executed as a simple script, the driver should be in `PATH`
            s = Service(
                executable_path='./chromedriver.exe')
            driver = webdriver.Chrome(
                service=s, chrome_options=chrome_options)

            def open_tab(driver, report):
                ActionChains(driver) \
                    .key_down(Keys.CONTROL) \
                    .key_down(Keys.SHIFT) \
                    .click(report) \
                    .key_up(Keys.CONTROL) \
                    .key_up(Keys.SHIFT) \
                    .perform()

        else:
            print('System is not compatible or something went wrong. Ask Kenny for help!')

        driver.headless = True
        driver.get("https://www.webselfstorage.com/SignIn")
        driver.maximize_window()
        driver.implicitly_wait(10)
        username = driver.find_element(By.XPATH, '//*[@id="userName"]')
        username.click()

        #Enter new username
        text = "kenneth_wf"
        for character in text:
            username.send_keys(character)
            time.sleep(0.1)  # pause for 0.3 seconds("kenneth_wf")
        driver.implicitly_wait(10)
        password = driver.find_element(By.XPATH, '//*[@id="Password"]')
        password.click()

        #Enter new password
        text = "Storage1!"
        for character in text:
            password.send_keys(character)
            time.sleep(0.1)  # pause for 0.3 seconds
        driver.implicitly_wait(10)
        signIn = driver.find_element(
            By.XPATH, '//*[@id="login_form"]/div/div[4]/input')
        signIn.click()
        driver.implicitly_wait(10)
        reports = driver.find_element(By.XPATH, '//*[@id="ctReports"]')
        reports.click()
        driver.implicitly_wait(10)

        #Collection Worksheet
        collectionWorksheet = driver.find_element(
            By.XPATH, '//*[@id="reportsListWidget"]/div/div[1]/div/ul/li[4]/a')

        open_tab(driver, collectionWorksheet)

        driver.implicitly_wait(10)
        driver.switch_to.window(driver.window_handles[1])
        driver.implicitly_wait(10)

        fromDays = driver.find_element(
            By.XPATH, '//*[@id="ReportArguments_FromDaysLate"]')
        fromDays.click()
        fromDays.clear()
        fromDays.send_keys('1')
        driver.implicitly_wait(10)

        fromDays = driver.find_element(
            By.XPATH, '//*[@id="ReportArguments_ToDaysLate"]')
        fromDays.click()
        fromDays.clear()
        fromDays.send_keys("999")
        fromDays.send_keys(Keys.ENTER)

        driver.implicitly_wait(10)

        #Occupancy Rate Exceptions

        driver.switch_to.window(driver.window_handles[0])

        driver.implicitly_wait(10)

        rateExceptions = driver.find_element(
            By.XPATH, '//*[@id="reportsListWidget"]/div/div[2]/div[3]/ul/li[1]/a')

        open_tab(driver, rateExceptions)

        driver.implicitly_wait(10)

        driver.switch_to.window(driver.window_handles[2])

        driver.implicitly_wait(10)

        driver.switch_to.window(driver.window_handles[0])

        #Management Summary
        driver.switch_to.window(driver.window_handles[0])

        driver.implicitly_wait(10)

        managementSummary = driver.find_element(
            By.XPATH, '//*[@id="reportsListWidget"]/div/div[3]/div[2]/ul/li[8]/a')
        open_tab(driver, managementSummary)
        driver.implicitly_wait(10)

        driver.switch_to.window(driver.window_handles[3])

        driver.implicitly_wait(10)
        printManagementSummary = driver.find_element(
            By.XPATH, '//*[@id="iframeContents"]/div/section/div/form/div[2]/div[2]/button')
        printManagementSummary.click()
        driver.implicitly_wait(10)

        #Occupancy Overview
        driver.switch_to.window(driver.window_handles[0])

        driver.implicitly_wait(10)
        occupancyOverview = driver.find_element(
            By.XPATH, '//*[@id="reportsListWidget"]/div/div[3]/div[2]/ul/li[11]/a')
        open_tab(driver, occupancyOverview)

        driver.switch_to.window(driver.window_handles[4])


if __name__ == "__main__":
    import sys
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    app = QtWidgets.QApplication(sys.argv)
    getReports = minneola.getReports()
