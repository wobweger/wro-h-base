
sUrl='https://ich.org/page/briefing-pack'

import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By


def fetchHtmlForThePage(url, delay, block_name):
    browser = webdriver.Firefox()
    browser.get(url)
    try:
        element_present = EC.presence_of_element_located((By.ID, block_name))
        WebDriverWait(browser, delay).until(element_present)
    except TimeoutException:
        print("Loading took too much time!")

    html = browser.page_source
    for a in browser.find_elements_by_xpath('.//a'):
        sLnk=a.get_attribute('href')
        if sLnk is None:
            continue
        try:
            print(sLnk)
            iPos=sLnk.rfind('.')
            if iPos>0:
                sExt=sLnk[iPos+1:]
                if sExt in ['doc','docx','pdf','ppt','xls','xlsx']:
                    a.click()
                    time.sleep(10)
        except:
            pass
    #browser.quit()
    return html


html = fetchHtmlForThePage(sUrl, 5, 're-Searchresult')
print(html)

oSoup=BeautifulSoup(html.content,'html.parser')


