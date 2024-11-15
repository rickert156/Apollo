from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time, csv
from tools.miniTools import createStartDir, firstStepPath, moveLink, LIST_LINK_DONE, readDoneLink 

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
    readDoneLink()
    driver.get('https://app.apollo.io/#/')
    with open(firstStepPath, 'r') as file:
        number_link = 0
        for row in csv.DictReader(file):
            domain = row['Domain']
            link = row['Link']
            if link not in LIST_LINK_DONE:
                number_link+=1
                print(f'[{number_link}] {link}')
                
                # Вот тут будет функция основного парсера
                # После него будет срабатывать moveLink
                
                moveLink(link)
                time.sleep(1)
            else:print(f'{link} уже обработал')


if __name__ == '__main__':
    createStartDir()
    main()
