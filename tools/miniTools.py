import os, shutil, csv
<<<<<<< HEAD
from tools.colors import RED, GREEN, RESET
=======
>>>>>>> 889a646 (Fix parser)

BASE_START_FILE = 'domain.csv'
BASE_DIR = 'Base'
DOMAIN_FILE_PATH = f'{BASE_DIR}/{BASE_START_FILE}'
DOMAIN_BASE = 'Domain'
RESULT_DIR = 'Result'
RESULT_FILE = 'apollo_result.csv'
TEMP_DIR = 'tmp'
TEMP_FILE = 'tmp.csv'
DONE_DIR = 'Done'
DONE_FILE = 'complite.txt'
COMPLETE_FILE = 'complite.csv'
COMPLETE_PATH = f'{DONE_DIR}/{COMPLETE_FILE}'
doneDomainFile = f'{DONE_DIR}/{DONE_FILE}'
FIRST_STEP_DIR = 'FirstStep'
FIRST_STEP_FILE = 'apollo_links.csv'
firstStepPath = f'{FIRST_STEP_DIR}/{FIRST_STEP_FILE}'
resultPath = f'{RESULT_DIR}/{RESULT_FILE}'

LIST_DOMAIN_DONE = []
LIST_LINK_DONE = []

# Создаем директории Result для хранения результатов
# и дирукторию Domain
def createStartDir():
    global DOMAIN_BASE, RESULT_DIR, DONE_DIR
    if not os.path.exists(BASE_DIR):os.makedirs(BASE_DIR);print(f'\tCREATE {GREEN}{BASE_DIR}{RESET}')
    if not os.path.exists(RESULT_DIR):os.makedirs(RESULT_DIR);(f'\tCREATE {GREEN}{RESULT_DIR}{RESET}')
    if not os.path.exists(DOMAIN_BASE):os.makedirs(DOMAIN_BASE);print(f'\tCREATE {GREEN}{DOMAIN_BASE}{RESET}')
    if not os.path.exists(DONE_DIR):os.makedirs(DONE_DIR);print(f'\tCREATE {GREEN}{DONE_DIR}{RESET}')
    if not os.path.exists(FIRST_STEP_DIR):os.makedirs(FIRST_STEP_DIR);print(f'\tCREATE {GREEN}{FIRST_STEP_DIR}{RESET}')
    if not os.path.exists(firstStepPath):
        with open(firstStepPath, 'a') as file:
            write = csv.writer(file)
            write.writerow(['Domain', 'Link'])
            print(f'\tCREATE {RED}{firstStepPath}{RESET}')
    if not os.path.exists(resultPath):
        with open(resultPath, 'a') as file:
            write = csv.writer(file)
            write.writerow(['Name', 'Email', 'Job Title', 'Company', 'Phone', 'Location'])
            print(f'\tCREATE {RED}{resultPath}{RESET}')
    if not os.path.exists(COMPLETE_PATH):
        with open(COMPLETE_PATH, 'a') as file:
            write = csv.writer(file)
            write.writerow(['Link'])
            print(f'\tCREATE {RED}{COMPLETE_PATH}{RESET}')
    if not os.path.exists(DOMAIN_FILE_PATH):
        with open(DOMAIN_FILE_PATH, 'a+') as file:
            write = csv.writer(file)
            write.writerow(['Company', 'Domain'])
            print(f'\tCREATE {RED}{DOMAIN_FILE_PATH}{RESET}')
    if not os.path.exists(doneDomainFile):
        with open(doneDomainFile, 'a+') as file:
            write = csv.writer(file)
            write.writerow('Domain')
            print(f'\tCREATE {RED}{doneDomainFile}{RESET}')
    

def createTempDir():
    global TEMP_DIR
    if not os.path.exists(TEMP_DIR):os.makedirs(TEMP_DIR)

def deleteTempDir():
    global TEMP_DIR
    if os.path.exists(TEMP_DIR):shutil.rmtree(TEMP_DIR)

def recordingPersonalData(targetFile, name, email, job, company, phone, location):
    with open(targetFile, 'a+') as file:
        write = csv.writer(file)
        write.writerow([name, email, job, company, phone, location])

def recordDomain(domain):
    global DONE_DIR, DONE_FILE
    with open(doneDomainFile, 'a+') as file:
        file.write(f'{domain}\n')
        
def checkDomain():
    global DONE_FILE, DONE_DIR, LIST_DOMAIN_DONE, doneDomainFile
    with open(doneDomainFile, 'r') as file:
        for domain in file.readlines():
            domain = domain.strip()
            LIST_DOMAIN_DONE+=[domain]

def recordingResultFirstStep(domain, link):
    global FIRST_STEP_DIR, FIRST_STEP_FILE, firstStepPath
    with open(firstStepPath, 'a+') as file:
        write = csv.writer(file)
        write.writerow([domain, link])

def moveLink(link):
    with open(COMPLETE_PATH, 'a+') as file:
        file.write(f'{link}\n')

def readDoneLink():
    global LIST_LINK_DONE
    with open(COMPLETE_PATH, 'r') as file:
        for row in csv.DictReader(file):
            link = row['Link']
            LIST_LINK_DONE+=[link]
