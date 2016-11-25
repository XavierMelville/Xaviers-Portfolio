from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


#chrome_options  = webdriver.chrome.options.Options()
#chrome_options.add_argument("--disable-extensions")
#chrome_options.add_argument("chrome.switches")
browser = webdriver.Firefox()
browser.get('http://127.0.0.1:8000')

assert 'Tiger' in browser.title
