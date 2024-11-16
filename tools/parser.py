from selenium.webdriver.common.by import By

def checkModal(driver):
    try:close_modal = driver.find_element(By.CLASS_NAME, 'zp_qe0Li.zp_S5tZC.zp_nQ45Z').click()
    except:pass

def clickButtonEmail(driver):
    try:button_email = driver.find_element(By.CLASS_NAME, 'zp-icon.apollo-icon.apollo-icon-download.zp_QUSTG.zp_K7tmh.zp_NGTfw').click()
    except:pass

def parserEmail(driver):
    try:email = driver.find_element(By.CLASS_NAME, 'zp_p2Xqs.zp_v565m.zp_N3Yvt.zp_kOWmA').text
    except:email = 'Not defined'
    finally:return email

def parserName(driver):
    try:
        name = driver.find_element(By.CLASS_NAME, 'zp_d9irS.EditTarget').text
        if '---' in name:name = name.split('---')[0]
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


def parserPhone(driver):
    try:phone = driver.find_element(By.CLASS_NAME, 'zp_p2Xqs.zp_v565m.zp_Pb8mt').text
    except:phone = 'Not defined'
    finally:return phone
