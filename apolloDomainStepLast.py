from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time, csv
from tools.miniTools import createStartDir, firstStepPath, moveLink, LIST_LINK_DONE, readDoneLink 
from tools.parser import parserName, parserJobTitle, parserLocation, parserCompany

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

def lead(driver):
    name = parserName(driver);print(f'Name: {name}')
    job = parserJobTitle(driver);print(f'Job Title: {job}')
    company = parserCompany(driver);print(f'Company: {company}')
    location = parserLocation(driver);print(f'Location: {location}')

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
                driver.get(link) 
                time.sleep(10)
                # Вот тут будет функция основного парсера
                # После него будет срабатывать moveLink
                lead(driver)
                moveLink(link)
                #time.sleep(10)
                input('sleep...')
            else:print(f'{link} уже обработал')


if __name__ == '__main__':
    createStartDir()
    main()
