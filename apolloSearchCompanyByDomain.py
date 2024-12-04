from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time, csv, os
from tools.miniTools import recordDomain, createStartDir, DONE_DIR, LIST_DOMAIN_DONE, checkDomain, recordingResultFirstStep
from tools.url import urlSearchCompany
from tools.colors import RED, GREEN, RESET

profileChrome = 'ProfileChrome'

chrome_options = Options()
# Подключение своего профиля
chrome_options.add_argument(f'user-data-dir={profileChrome}')
chrome_options.add_argument("--disable-blink-features")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_argument("start-maximized")


def parserCompanyName(driver, name, email, domain):
    try:company_name = driver.find_element(By.CLASS_NAME, 'zp_p2Xqs.zp_v565m.zp_PS1Pb').text
    except:company_name = 'N/A'
    
    if not os.path.exists('Clutch.csv'):
        with open('Clutch.csv', 'a') as file:
            write = csv.writer(file)
            write.writerow(['Name', 'Email', 'Domain', 'Company'])

    if company_name != 'N/A':
        with open('Clutch.csv', 'a+') as file:
            write = csv.writer(file)
            write.writerow([name, email, domain, company_name])
            print(f'{RED}{name}:{RESET} {GREEN}{company_name}{RESET}')
        
    


def main():
    LIST_DOMAIN = []
    driver = webdriver.Chrome(options=chrome_options)
    baseDir, domainDoc, domain = 'Base', 'domain.csv', False
    targetBase = f'{baseDir}/{domainDoc}'
    
    driver.get('https://app.apollo.io')
    time.sleep(1)
    try:
        with open(f'Clutch.csv', 'r') as file:
            for row in csv.DictReader(file):
                domain = row['Domain']
                LIST_DOMAIN+=[domain]
    except:pass
    #input('...')
    with open(targetBase, 'r') as file:
        number_domain = 0
        for row in csv.DictReader(file):
            checkDomain()
            name = row['Name']
            domain = row['Domain']
            email = row['Email']
            if domain not in LIST_DOMAIN:
                number_domain+=1
                driver.get(urlSearchCompany(domain))
                time.sleep(5)
                print(f'[{number_domain}] {domain}')
                parserCompanyName(driver, name, email, domain)
                time.sleep(5)
            else:print(f'{RED}{domain} уже обработан{RESET}')


if __name__ == '__main__':
    createStartDir()
    main()
