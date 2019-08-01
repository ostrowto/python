# Simply random generator

import string, sys
from datetime import datetime
from random import *

print('''

************************************************************************************
*                            PASSWORD GENERATOR 1.0                                *                          
************************************************************************************

''')

randomize_numbers = string.ascii_uppercase + string.ascii_lowercase + string.digits

psswd_1 = "".join(choice(randomize_numbers) for a in range(randint(8,9)))
psswd_2 = "".join(choice(randomize_numbers) for a in range(randint(8,9)))
psswd_3 = "".join(choice(randomize_numbers) for a in range(randint(8,9)))

filename_datetime = datetime.now().strftime("%Y%m%d-%H%M%S")

print(' ')
print('Your randomize password are: ')
print(' ')
print('First standard 9 characters password:            ', psswd_1)
print(' ')
print('Seccond standard 9 characters password:          ', psswd_2)
print(' ')
print('Third standard 9 characters password:            ', psswd_3)
print(' ')
print('Concatenated very strong 27 characters password: ', psswd_1 + psswd_2 + psswd_3)
print(' ')
print('Please press any key to end, and a password file ' + ' "Your_Password.txt" ' + ' will be created.')
print('Date and time of creation: ', filename_datetime)
input()

sys.stdout = open('Your_Password.txt', 'w')
print('Date and time of creation: ', filename_datetime)
print('Concatenated very strong 27 characters password: ', psswd_1 + psswd_2 + psswd_3)
sys.stdout.close() 