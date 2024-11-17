import os
from tools.colors import RED, GREEN, YELLOW, BLUE, RESET
from apolloSearchByDomain import main as mode_search_by_domain
from apolloSearchLead import main as mode_classic
from apolloStepLast import main as mode_final_collection

def main():
    try:
        selectMode = str(input(f"""
    {YELLOW}Apollo: Version 3{RESET}
    
        {YELLOW}MENU:{RESET}
        
        {RED}[1]{RESET} {GREEN}Mode: Classic{RESET}\t{RED}[2]{RESET} {GREEN}Mode: Search by domain{RESET}

        {RED}[3]{RESET} {GREEN}Mode: Final data collection{RESET}

    {RED}Select Mode:{RESET} """))
        selectMode = selectMode.strip()
        if selectMode == '1':mode_classic()
        if selectMode == '2':mode_search_by_domain()
        if selectMode == '3':mode_final_collection()
        else:print('[x]_0')
    except KeyboardInterrupt:print('\nВыход из программы')

if __name__ == '__main__':
    main()
