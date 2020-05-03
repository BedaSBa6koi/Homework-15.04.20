year = int(input('Enter year '))

def bissextile(year):
    if year % 4 != 0:
        print(year, 'is usual year')
    elif year % 100 == 0:
        if year % 400 == 0:
            print(year, 'is intercalary year')
        else:
            print(year, 'is usual year')
    else:
        print(year, 'is intercalary year')
    return year

bissextile(year)
