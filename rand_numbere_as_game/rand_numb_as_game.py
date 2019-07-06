#rand_numb_as_game

import random

lottery_Numbers = []
for i in range(0,6):
    number = random.randint(1,50)
    while number in lottery_Numbers:
        number = random.randint(1,50)
    lottery_Numbers.append(number)

lottery_Numbers.sort()


user_Numbers = []
for i in range(0,6):
    number = int(input('Please enter a number between 1 and 49 \n'))
    while number<1 or number>49:
        number = int(input('Please try agin: enter a correct number between 1 and 49 \n'))
    user_Numbers.append(number)

user_Numbers.sort()



print('Your lottery numbers are: ')
print(lottery_Numbers)

print('Your selection: ')
print(user_Numbers)


counter = 0
for number in user_Numbers:
    if number in lottery_Numbers:
        counter +=1

print('You have guessed ' + str(counter) + ' number(s) correctly')

compare_list = []
for element in lottery_Numbers:
    if element in user_Numbers:
        compare_list.append(element)

print('Your lucky numbers are: ', compare_list)

print('Please enter any key for exit... ')
input()