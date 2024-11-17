def url(domain):
    url = f'https://app.apollo.io/#/people?page=1&qKeywords={domain}&sortAscending=false&sortByField=%5Bnone%5D&personSeniorities[]=owner&personSeniorities[]=founder&personSeniorities[]=director&personSeniorities[]=head'
    return url


def urlSearch(page, job, location, industry, minEmpl, maxEmpl):
    url = f'https://app.apollo.io/#/people?sortAscending=false&sortByField=[none]&page={page}&personSeniorities[]={job}&personLocations[]={location}&organizationIndustryTagIds[]={industry}&organizationNumEmployeesRanges[]={minEmpl},{maxEmpl}'
    return url
