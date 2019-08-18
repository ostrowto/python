#num_generator.py

import sys

range_you_wish = int(input('What range do you wish? '))

list = []

for i in range(range_you_wish+1):
    list.append(i)

sys.stdout = open('list_of_numbers.txt', 'w')
print(list[:])
sys.stdout.close() 

