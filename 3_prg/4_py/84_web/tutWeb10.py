from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
import time

print("******************************** STARTING ********************************")

display = Display(visible=0, size=(1024, 768))
display.start()

# To prevent download dialog
profile = webdriver.FirefoxProfile()
profile.set_preference('browser.download.folderList', 2) # custom location
profile.set_preference('browser.download.manager.showWhenStarting', False)
profile.set_preference('browser.download.dir', '/srv/download')
profile.set_preference("browser.download.manager.alertOnEXEOpen", False)
profile.set_preference("browser.download.manager.closeWhenDone", False)
profile.set_preference("browser.download.manager.focusWhenStarting", False)
#application/octet-stream,application/vnd.ms-excel 
profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/x-msdownload,application/octet-stream')
try:
    browser = webdriver.Firefox(profile)
    browser.get('https://www.7-zip.org/')
    download_button = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'td.Item a')))
    download_button.click()
    print("clicked...")
    time.sleep(10) 
    print (os.listdir("/srv/download"))
except Exception as ex:
    print(ex)
 
browser.close()
display.stop()


print("******************************** FINITO ********************************")
