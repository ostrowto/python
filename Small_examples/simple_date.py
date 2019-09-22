# simple date

from datetime import datetime, timedelta

today = datetime.now()

current_date = datetime.now()

print('Today is: ' + str(current_date))


one_day = timedelta(days = 1)
yesterday = today - one_day

print('Yesterday was: ' + str(yesterday))


print('Day: ' + str(current_date.day))
print('Month: ' + str(current_date.month))
print('Year: ' + str(current_date.year))

birthday_calc = input('When is your birthday (dd/mm/yyyy)? ')

birthday_date = datetime.strptime(birthday_calc, '%d/%m/%Y')
print('Your birthday: ' + str(birthday_date))