
import requests
from bs4 import BeautifulSoup

sUrl='https://ich.org/page/briefing-pack'

#html=requests.get(sUrl)
#oSoup=BeautifulSoup(html.content,'html.parser')


#import selenium compnents, urllib, beautiful soup
from bs4 import BeautifulSoup
from selenium import webdriver
from urllib import urlopen
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By


#url - the url to fetch dynamic content from.
#delay - second for web view to wait
#block_name - id of the tag to be loaded as criteria for page loaded state.
def fetchHtmlForThePage(url, delay, block_name):
	#supply the local path of web driver.
	#in this example we use chrome driver
	browser = webdriver.Chrome('/Applications/chromedriver')
	#open the browser with the URL
	#a browser windows will appear for a little while
	browser.get(url)
	try:
	#check for presence of the element you're looking for
		element_present = EC.presence_of_element_located((By.ID, block_name))
		WebDriverWait(browser, delay).until(element_present)

	#unless found, catch the exception
	except TimeoutException:
		print "Loading took too much time!"	

	#grab the rendered HTML
	html = browser.page_source
	#close the browser
	browser.quit()
	#return html
	return html


#call the fetching function we created
html = fetchHtmlForThePage(sUrl, 5, 're-Searchresult')
#grab HTML document
soup = BeautifulSoup(html)
#process it further as you wish.....
#.....
processFetchedUrls(soup, path)
