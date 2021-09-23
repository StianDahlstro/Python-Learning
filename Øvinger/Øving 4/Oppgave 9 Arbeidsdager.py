# Oppgave 9
# Arbeidsdager
weekdayStartYear = []

def isLeapYear(_year):
    if _year % 400 == 0:
        return True
    elif _year % 100 == 0:
        return False
    elif _year % 4 == 0:
        return True
    return False

def weekdayNewyear(_yearStart, _yearEnd):
    count= 0
    day = [
        'Mandag', 'Tirsdag', 'Onsdag', 'Torsdag', 'Fredag', 'Lørdag', 'Søndag'
    ]
    for i in range(_yearStart, _yearEnd + 2):
        print(i, day[count % len(day)])
        weekdayStartYear.append(day[count % len(day)])
        if isLeapYear(i) == True:
            count += 1
        count += 1

def isWorkday(_dag):
    day = [
        'Mandag', 'Tirsdag', 'Onsdag', 'Torsdag', 'Fredag', 'Lørdag', 'Søndag'
    ]
    if day[_dag - 1] == 'Lørdag' or day[_dag - 1] == 'Søndag':
        return False
    return True


def workdaysInYear(_yearStart, _yearEnd):
    weekday = [
        'Mandag', 'Tirsdag', 'Onsdag', 'Torsdag', 'Fredag'
    ]
    weekend = [
        'Lørdag', 'Søndag'
    ]
    count = 0
    for i in range(_yearStart, _yearEnd + 1):
        workdaysNonLeapYear = 52 * 5
        if isLeapYear(i) == True:
            workdaysNonLeapYear += 1
        if weekdayStartYear[count] in weekday and weekdayStartYear[count + 1] in weekday:
            workdaysNonLeapYear += 1
        if weekdayStartYear[count] in weekend and weekdayStartYear[count + 1] in weekday:
            workdaysNonLeapYear -= 1
        if weekdayStartYear[count] in weekday and weekdayStartYear[count + 1] in weekend and isLeapYear(i) == True:
            workdaysNonLeapYear -= 1
        if (weekdayStartYear[count] in weekday and weekdayStartYear[count + 1] in weekend):
            workdaysNonLeapYear += 1
        if weekdayStartYear[count] == 'Søndag' and weekdayStartYear[count + 1] == 'Mandag':
            workdaysNonLeapYear += 1

        count += 1
        print(f'{i} has {workdaysNonLeapYear} workdays.')



yearStart = int(input('Enter a year to start from: '))
yearEnd = int(input('Enter a year to end on: '))
weekdayNewyear(yearStart, yearEnd)
workdaysInYear(yearStart, yearEnd)

day = int(input("Enter a day in numeral form to check if it's a workday or not [Monday is 1, Tuesday is 2...]: "))
print(isWorkday(day))