# list_generator.py

import sys
from datetime import datetime

print('-' * 30)
print('Simple number generator:')
print('1. Program generate a series of numbers in one vertical column.')
print('2. The program asks you to enter the starting number, ending number and step of the move.')
print('3. The program will create a .txt file with the result.')
print('4. The program automatically finishes its work.')
print('5. Remember! use only whole numbers, You can use negative numbers.')
print('-' * 30)

# Define inputs

start_number = int(input('Please define start number? '))
end_number = int(input('Please define end number '))
step_by = int(input('Please define a step by value '))

# Logic :)

myNumbers = list(range(start_number, end_number, step_by))

# End

filename_datetime = datetime.now().strftime("\n\n\tDate: %Y-%m-%d Time: %H:%M:%S")

sys.stdout = open('Your_list.txt', 'w')
print("Your numbers in list are: \n\n\t", ' \n\t '.join(map(str, myNumbers[:])))
print(' ')
print('Date and time of creation: ', filename_datetime)
sys.stdout.close()