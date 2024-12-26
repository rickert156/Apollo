from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time, csv
from tools.colors import RED, RESET, GREEN, YELLOW, BLUE
from tools.miniTools import createStartDir, firstStepPath, moveLink, LIST_LINK_DONE, readDoneLink, recordingPersonalData, resultPath
from tools.parser import parserName, parserJobTitle, parserLocation, parserCompany, parserEmail, parserPhone, checkModal, clickButtonEmail
from config import service_parser, category

profileChrome = 'ProfileChrome'

chrome_options = Options()
# Подключение своего профиля
chrome_options.add_argument(f'user-data-dir={profileChrome}')
chrome_options.add_argument("--disable-blink-features")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_argument("start-maximized")


def lead(driver):
    global resultPath

    checkModal(driver)
    clickButtonEmail(driver);time.sleep(5)

    name = parserName(driver);print(f'{GREEN}Name: {name}{RESET}')
    email = parserEmail(driver);print(f'{GREEN}Email: {email}{RESET}')
    job = parserJobTitle(driver);print(f'{GREEN}Job Title: {job}{RESET}')
    company = parserCompany(driver);print(f'{GREEN}Company: {company}{RESET}')
    phone = parserPhone(driver);print(f'{GREEN}Phone: {phone}{RESET}')
    location = parserLocation(driver);print(f'{GREEN}Location: {location}{RESET}\n')
    
    if '@' in email:
        recordingPersonalData(resultPath, name, email, job, company, phone, location, category, service_parser)
        print(f'{YELLOW}Data recorded{RESET}\n')

def main():
    driver = webdriver.Chrome(options=chrome_options)
    readDoneLink()
    driver.get('https://app.apollo.io/#/')
    with open(firstStepPath, 'r') as file:
        number_link, complite_link = 0, 0
        for row in csv.DictReader(file):
            link = row['Link']
            if link not in LIST_LINK_DONE:
                number_link+=1
                print(f'[{number_link}] {link}')
                driver.get(link) 
                time.sleep(10)
                lead(driver)
                moveLink(link)
                time.sleep(20)
            else:complite_link+=1;print(f'{BLUE}[{complite_link}]{link} Complete{RESET}')


if __name__ == '__main__':
    createStartDir()
    main()
