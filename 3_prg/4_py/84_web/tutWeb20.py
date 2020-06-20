
sUrl='https://ich.org/page/briefing-pack'
#sUrl='https://my.syncplicity.com/Files/'

import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

options = webdriver.ChromeOptions()
#options.add_argument('--ignore-certificate-errors')
#options.add_argument("--test-type")
#options.binary_location = "/usr/bin/chromium"
#options.binary_location = "C:\Program Files\Mozilla Firefox\firefox.exe"
driver = webdriver.Chrome(chrome_options=options)
#driver = webdriver.Firefox()

driver.get(sUrl)
for iOfs in range(10):
    time.sleep(1)
    
#WebDriverWait.delay(driver,10)
for a in driver.find_elements_by_xpath('.//a'):
    print(a.get_attribute('href'))

