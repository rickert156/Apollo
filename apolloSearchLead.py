from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time, csv
from tools.url import urlSearch
from tools.miniTools import createStartDir
from tools.menu import menu
from tools.parameters import testing

profileChrome = 'ProfileChrome'

chrome_options = Options()
# Подключение своего профиля
chrome_options.add_argument(f'user-data-dir={profileChrome}')
chrome_options.add_argument("--disable-blink-features")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_argument("start-maximized")

driver = webdriver.Chrome(options=chrome_options)

def main():
    driver.get('https://app.apollo.io/#/')
    
    menu()

    # Пример
    test_url = urlSearch(1, 'owner', 'United States', '5567cd4e7369643b70010000', 1, 200)
    driver.get(test_url)
    input('...')

if __name__ == '__main__':
    createStartDir()
    main()
