import time
import platform

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

op_sys = platform.system()

if(op_sys == Darwin):
    service = 

else()
    service = Service('"D:\chromedriver.exe"')

service.start()

driver = webdriver.Remote(service.service_url)

driver.get('http://www.google.com/');

time.sleep(5) # Let the user actually see something!

driver.quit()
