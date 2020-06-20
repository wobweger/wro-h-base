
sUrl='https://ich.org/page/briefing-pack'

import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import PySimpleGUI as sg

layout = [[sg.T('Download files', size=(30,1), font='Any 15')],      
        [sg.T('url'), sg.In(sUrl,key='sUrl', size=(40,1)),sg.Button('download')],
        [sg.T('file'), sg.In('', size=(60,1), key='sFN'),sg.Button('oky'),sg.Button('skp')],
        [sg.Button('Exit', size=(10, 1) )]  
        #[sg.Button('Exit', size=(10, 2), pad=((280, 0), 3), font='Helvetica 14')]  
        ]

lyQst = [[sg.T('Download files', size=(30,1), font='Any 15')],      
        [sg.T('url'), sg.In(key='sUrl'),],
        [sg.T('file'), sg.In('', size=(200,1), key='sFN')],
        [sg.Button('oky'),sg.Button('skp')],
        [sg.Button('Exit', size=(10, 2), pad=((280, 0), 3), font='Helvetica 14')]  
        ]


def fetchHtmlForThePage(url, delay, block_name,winQst):
    profile = webdriver.FirefoxProfile()
    profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/x-msdownload,application/octet-stream')
    browser = webdriver.Firefox(profile)
    browser.get(url)
    try:
        element_present = EC.presence_of_element_located((By.ID, block_name))
        WebDriverWait(browser, delay).until(element_present)
    except TimeoutException:
        print("Loading took too much time!")
    #winQst = sg.Window('Downloader', layout, 
    #                grab_anywhere=False)  
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
                    iOfsFN=sLnk.rfind('/')
                    if iOfsFN>0:
                        winQst['sFN'].update(sLnk[iOfsFN:])
                    else:
                        winQst['sFN'].update(sLnk)
                    event, values = winQst.read()      
                    if event is None:      
                        break
                    elif event == 'oky':
                        a.click()
                        time.sleep(.5)
                    elif event == 'Exit':
                        break
        except:
            pass
    #browser.quit()
    return html

window = sg.Window('Downloader', layout, 
                auto_size_text=False, 
                default_element_size=(10,1),      
                text_justification='r', 
                return_keyboard_events=True, 
                grab_anywhere=False)  
#window['sUrl'].update(sUrl)

while True:      
    event, values = window.read()      
    if event is None:      
        break
    if event=='Exit':      
        break
    elif event == 'download':
        sUrl = values['sUrl']
        html = fetchHtmlForThePage(sUrl, 5, 're-Searchresult',window)
        #print(html)

#oSoup=BeautifulSoup(html.content,'html.parser')


