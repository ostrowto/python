# iterator to list
import sys, random

first_number = int(input('First number to start'))
second_number = int(input('Second number to start'))
third_number = int(input('Third number to start'))
fourth_number = int(input('Fourth number to start'))


list = []

for i in range((random.randint(first_number, second_number)), (random.randint(third_number, fourth_number))):
    list.append(i)

sys.stdout = open('List.txt', 'w')
print(list)

