from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time, csv
from tools.miniTools import recordDomain, createStartDir, DONE_DIR, LIST_DOMAIN_DONE, checkDomain, recordingResultFirstStep
from tools.url import url

profileChrome = 'ProfileChrome'

chrome_options = Options()
# Подключение своего профиля
chrome_options.add_argument(f'user-data-dir={profileChrome}')
chrome_options.add_argument("--disable-blink-features")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_argument("start-maximized")


def main():
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://app.apollo.io')
    input('Login...')
    
if __name__ == '__main__':
    createStartDir()
    main()
