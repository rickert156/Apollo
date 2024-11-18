from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time, csv
# Мои модули
from tools.miniTools import createStartDir, BASE_START_FILE, BASE_DIR, createTempDir, deleteTempDir

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

SET_DOMAIN = set()

#
# ПОКА ЧТО НЕ РАЗОБРАЛСЯ С ФРЕЙМОМ
#

def iframeApollo(driver):
    time.sleep(15)
    try:
        iframe = driver.find_element(By.TAG_NAME, 'iframe')
        driver.switch_to.frame(iframe)
        print('[+] iframe Обнаружен!')
        openExtension = driver.find_element(By.CLASS_NAME, 'zp-button.x_GGHzP.x_Ak05C.x_RJ9V0.x_cm9L2.x_KDi47')
        
        action = ActionChains(driver)
        action.move_to_element(openExtension).perform()
        action.click()
        time.sleep(2)
        #openExtension.click()
        time.sleep(2)
        driver.switch_to.default_content()
    except Exception as err:
        print(f'[-] iframe Не Обнаружен!\nError: {err}')


def main():
    global BASE_START_FILE, BASE_DIR, SET_DOMAIN
    createStartDir()
    
    driver.get('https://google.com')
    
    startFile = f'{BASE_DIR}/{BASE_START_FILE}'
    with open(startFile, 'r') as file:
        number_domain = 0
        for row in csv.DictReader(file):
            domain = row['Domain']
            company = row['Company']
            if '.' in domain:
                number_domain+=1
                SET_DOMAIN.add(domain)
                print(f'[{number_domain}] {domain}')
        print('End...')

    # Отладка парсинга данных с расширения
    import random
    randDomain = random.choice(list(SET_DOMAIN))
    site = f'http://{randDomain}'
    driver.get(site)
    print(f'\nSite: {site}')
    iframeApollo(driver)
    input('...')


if __name__ == '__main__':
    main()
