def url(domain):
    url = f'https://app.apollo.io/#/people?page=1&qKeywords={domain}&sortAscending=false&sortByField=%5Bnone%5D&personSeniorities[]=owner&personSeniorities[]=founder&personSeniorities[]=director&personSeniorities[]=head'
    return url


def urlSearch(page, industry, job, location, minEmpl, maxEmpl):
    url = (f'https://app.apollo.io/#/people?sortAscending=false'
            f'&sortByField=%5Bnone%5D&personSeniorities[]={job}'
            f'&organizationNumEmployeesRanges[]={minEmpl}%2C{maxEmpl}'
            f'&organizationIndustryTagIds[]={industry}'
            f'&personLocations[]={location}'
            f'&page={page}') 
    print(url)
    return url

def urlSearchCompany(domain):
    url = f'https://app.apollo.io/#/companies?page=1&sortAscending=false&sortByField=recommendations_score&qOrganizationName={domain}'
    return url


