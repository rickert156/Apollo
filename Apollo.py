import os
from tools.colors import RED, GREEN, YELLOW, BLUE, RESET
from tools.miniTools import createStartDir
from apollo.apolloSearchByDomain import main as mode_search_by_domain
from apollo.apolloSearchLead import main as mode_classic
from apollo.apolloStepLast import main as mode_final_collection
from apollo.login import main as mode_login 

def main():
    try:
        selectMode = str(input(f"""
    {YELLOW}Apollo: Version 3{RESET}
    
        {YELLOW}MENU:{RESET}
        
        {RED}[1]{RESET} {GREEN}Mode: Classic{RESET}\t{RED}[2]{RESET} {GREEN}Mode: Search by domain{RESET}

        {RED}[3]{RESET} {GREEN}Mode: Final Step{RESET}\t{RED}[4]{RESET} {GREEN}Mode: Login Account{RESET}

    {RED}Select Mode:{RESET} """))
        selectMode = selectMode.strip()
        if selectMode == '1':createStartDir();mode_classic()
        if selectMode == '2':createStartDir();mode_search_by_domain()
        if selectMode == '3':createStartDir();mode_final_collection()
        if selectMode == '4':createStartDir();mode_login()
        else:print('[x]_0')
    except KeyboardInterrupt:print('\nВыход из программы')

if __name__ == '__main__':
    main()
