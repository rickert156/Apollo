def Industry(params):
    params = params.strip()
    params = str(params)
    if params == '1':params = '5567cd877369644cf94b0000'
    if params == '2':params = '5567cdb773696439a9080000'
    
    else:params = '5567cd877369644cf94b0000' # Computer & Network Security
    print(f'[*] {params} [*]')
    return params


def JobTitle(params):
    params = params.strip()
    params = str(params)
    if params == '1':params = 'owner'
    if params == '2':params = 'founder'
    if params == '3':params = 's_suite'
    if params == '4':params = 'partner'
    if params == '5':params = 'vp'
    if params == '6':params = 'head'
    if params == '7':params = 'director'

    #else:params = 'owner'
    print(f'[*] {params} [*]')
    return params


def Location(params):
    params = params.strip()
    params = str(params)
    if params == '1':params = 'United States'
    if params == '2':params = 'Canada'
    if params == '3':params = 'Australia'
    if params == '4':params = 'United Kingdom'
    if params == '5':params = 'Russia'
    if params == '6':params = 'Ukraine'

    else:params = 'United States'
    print(f'[*] {params}  [*]')
    return params


def MinEmpl(params):
    if params != False:params = params
    
    else:params = '1'
    print(f'[*] {params}  [*]')
    return params

def MaxEmpl(params):
    if params != False:params = params
    
    else:params = '2000'
    print(f'[*] {params}  [*]')
    return params