from selenium.webdriver.common.by import By

def parserName(driver):
    try:name = driver.find_element(By.CLASS_NAME, 'zp_d9irS.EditTarget').text
    except:name = 'Not defined'
    finally:return name

def parserJobTitle(driver):
    try:job = driver.find_element(By.CLASS_NAME, 'zp_usEUk').text
    except:job = 'Not defined'
    finally:return job

def parserLocation(driver):
    try:location = driver.find_element(By.CLASS_NAME, 'zp_U0WNp').text
    except:location = 'Not defined'
    finally:return location

def parserCompany(driver):
    try:company = driver.find_element(By.CLASS_NAME, 'zp_HN__y').text
    except:company = 'Not defined'
    finally:return company
