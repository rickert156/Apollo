import os, shutil, csv

BASE_START_FILE = 'domain.csv'
BASE_DIR = 'Base'
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
    if not os.path.exists(RESULT_DIR):os.makedirs(RESULT_DIR)
    if not os.path.exists(DOMAIN_BASE):os.makedirs(DOMAIN_BASE)
    if not os.path.exists(DONE_DIR):os.makedirs(DONE_DIR)
    if not os.path.exists(FIRST_STEP_DIR):os.makedirs(FIRST_STEP_DIR)
    if not os.path.exists(doneDomainFile):open(doneDomainFile, 'a').close()
    if not os.path.exists(firstStepPath):
        with open(firstStepPath, 'a') as file:
            file.write(f'Domain,Link')
    if not os.path.exists(resultPath):
        with open(resultPath, 'a') as file:
            file.write('Name,Email,Job Title,Location')
    if not os.path.exists(COMPLETE_PATH):
        with open(COMPLETE_PATH, 'a') as file:
            file.write('Link\n')

# Содаем временную директорию для хранения данных
def createTempDir():
    global TEMP_DIR
    if not os.path.exists(TEMP_DIR):os.makedirs(TEMP_DIR)

# Удаляем временную директорию
def deleteTempDir():
    global TEMP_DIR
    if os.path.exists(TEMP_DIR):shutil.rmtree(TEMP_DIR)


# Шаблон записи данных в таблицу
# Пока что не используется, для второго этапа
def recordingPersonalData(targetFile, name, email, job, location):
    with open(targetFile, 'a+') as file:
        write = csv.writer(file)
        write.writerow([name, email, job, location])

# Записываем домен в файлик, что бы
# можно было отслеживать пройденные
def recordDomain(domain):
    global DONE_DIR, DONE_FILE
    with open(doneDomainFile, 'a+') as file:
        file.write(f'{domain}\n')
        
# Чтение файла с уже обработанными доменами
def checkDomain():
    global DONE_FILE, DONE_DIR, LIST_DOMAIN_DONE, doneDomainFile
    with open(doneDomainFile, 'r') as file:
        for domain in file.readlines():
            domain = domain.strip()
            LIST_DOMAIN_DONE+=[domain]

# Запись данных с первого этапа
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
