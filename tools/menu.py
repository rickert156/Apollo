from tools.colors import RED, GREEN, BLUE, YELLOW, RESET
from tools.parameters import Industry, JobTitle, Location, MinEmpl, MaxEmpl

def menu():
    industry = str(input(f"""\
    {GREEN}Select Industry: 
        1. Computer & Network Security
        2. Capital Markets
        3. Banking
        4. Computer Games
        5. Computer Software
        6. Investment Management
        7. Graphic Design
        8. Alternative medicine
        9. Broadcast media
        10. Business supplies & Equipment(товары и оборудование для бизнеса)
        11. Сommercial real estate 
        >>> {RESET}"""))
    industry  = Industry(industry)
    
    job = str(input(f"""\
    {GREEN}Select Job Title: 
        1. Owner
        2. Founder
        3. C suite
        4. Partner
        5. VP
        6. Head
        7. Director
        >>> {RESET}"""))
    jobTitle = JobTitle(job)

    location = str(input(f"""\
    {GREEN}Select Location:
        1. United States
        2. Canada
        3. Australia
        4. United Kingdom
        5. Russia
        6. Ukraine
        >>> {RESET}"""))
    location = Location(location)

    minEmpl = input(f'{GREEN}Minimum number of employees: {RESET}')
    minEmpl = MinEmpl(minEmpl)

    maxEmpl = input(f'{GREEN}Maximum number of employees: {RESET}')
    maxEmpl = MaxEmpl(maxEmpl)

    maxPage = input(f'{GREEN}How many pages: {RESET}')

    return industry, jobTitle, location, minEmpl, maxEmpl, maxPage
