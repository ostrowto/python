# password_generator

import sys, random

def shuffle(string):
    temp_Numbers = list(string)
    random.shuffle(temp_Numbers)
    return ''.join(temp_Numbers)


letter_1 = chr(random.randint(65,90))
letter_2 = chr(random.randint(65,90))
letter_3 = chr(random.randint(65,90))
letter_4 = chr(random.randint(65,90))
letter_5 = chr(random.randint(65,90))
letter_6 = chr(random.randint(65,90))
letter_7 = chr(random.randint(65,90))
letter_8 = chr(random.randint(65,90))
letter_9 = chr(random.randint(65,90))
letter_10 = chr(random.randint(65,90))
letter_11 = chr(random.randint(65,90))
letter_12 = chr(random.randint(65,90))


password = letter_1 + letter_2 + letter_3 + letter_4 + letter_5 + letter_6 + letter_7 + letter_8 + letter_9 + letter_10 + letter_11 + letter_12
password = shuffle(password)

print(password)

sys.stdout = open('Your_Password.txt', 'w')
print(password)

