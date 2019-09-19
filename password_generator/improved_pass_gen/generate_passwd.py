# generate_passwd.py

import string
from random import choice


numbers_of_digits = int(input('How long password? '))
alpha_Symbols = string.ascii_letters + string.digits
password = ''.join(choice(alpha_Symbols) for i in range(numbers_of_digits))
print(password)