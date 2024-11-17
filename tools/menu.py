from tools.colors import RED, GREEN, BLUE, YELLOW, RESET

def menu():
    industry = input(f"""\
    {GREEN}Select Industry: 
        1. Computer & Network Security
        2. Capital Markets
        >>> {RESET}""")
    
    job = input(f"""\
    {GREEN}Select Job Title: 
        1. Owner
        2. Founder
        3. C suite
        4. Partner
        5. VP
        6. Head
        7. Director
        >>> {RESET}""")

    location = input(f"""\
    {GREEN}Select Location:
        1. United States
        2. Canada
        3. Australia
        4. United Kingdom
        5. Russia
        6. Ukraine
        >>> {RESET}""")
    
    minEmpl = input(f'{GREEN}Minimum number of employees: {RESET}')
    
    maxEmpl = input(f'{GREEN}Maximum number of employees: {RESET}')

    maxPage = input(f'{GREEN}How many pages: {RESET}')
