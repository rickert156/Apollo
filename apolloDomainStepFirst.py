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

driver = webdriver.Chrome(options=chrome_options)

def parserLinks(driver, domain):
    SET_LINK = set()
    patternLink, antiPattern = '#/people/', '/tags'
    try:
        number_link = 0
        time.sleep(3)
        for links in driver.find_elements(By.TAG_NAME, 'a'):
            link = links.get_attribute('href')
            if patternLink in link and antiPattern not in link:
                if '?' in link:link = link.split('?')[0]
                SET_LINK.add(link)
        for link in SET_LINK:
            number_link+=1
            recordingResultFirstStep(domain, link)
            print(f'\t[{number_link}] {link}')
    except Exception as err:print(f'Error: {err}')

def main():
    baseDir, domainDoc, domain = 'Base', 'domain.csv', False
    targetBase = f'{baseDir}/{domainDoc}'
    
    driver.get('https://app.apollo.io')
    time.sleep(1)

    #input('...')
    with open(targetBase, 'r') as file:
        number_domain = 0
        for row in csv.DictReader(file):
            checkDomain()
            domain = row['Domain']
            if domain not in LIST_DOMAIN_DONE:
                number_domain+=1
                driver.get(url(domain))
                print(f'[{number_domain}] {domain}')
                parserLinks(driver, domain)
                recordDomain(domain)
                time.sleep(5)
            else:print(f'{domain} уже обработан')


if __name__ == '__main__':
    createStartDir()
    main()
