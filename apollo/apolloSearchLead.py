from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time, csv
from tools.menu import menu
from tools.url import urlSearch
from tools.miniTools import createStartDir, recordingResultFirstStep

profileChrome = 'ProfileChrome'

chrome_options = Options()
# Подключение своего профиля
chrome_options.add_argument(f'user-data-dir={profileChrome}')
chrome_options.add_argument("--disable-blink-features")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_argument("start-maximized")


def parserLinks(driver):
    SET_LINK = set()
    patternLink, antiPattern = '#/people/', '/tags'
    print('Пауза в 15 секунд')
    time.sleep(15)
    print('Начинаем собирать ссылки')
    try:
        for links in driver.find_elements(By.TAG_NAME, 'a'):
            links = links.get_attribute('href')
            if patternLink in links and antiPattern not in links:
                if '?' in links:links = links.strip('?')[0]
                if 'http' in links:SET_LINK.add(links)
        number_link = 0
        for link in SET_LINK:
            number_link+=1
            print(f'[{number_link}] {link}')
            recordingResultFirstStep(number_link, link)
    except Exception as err:print(f'Error: {err}')



def main():
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://app.apollo.io/#/')
    
    industry, jobTitle, location, minEmpl, maxEmpl, maxPage = menu()
    pushinka = '-'*20
    for page in range(1, int(maxPage)+1):
        urlRequest = urlSearch(page, industry, jobTitle, location, minEmpl, maxEmpl)
        print(f'{pushinka} Page {page} {pushinka}')
        driver.get(urlRequest)
        driver.refresh()
        parserLinks(driver)
        time.sleep(10)

if __name__ == '__main__':
    createStartDir()
    main()
