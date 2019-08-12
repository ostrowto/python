# random_choice.py

import random, sys
from datetime import datetime

print('''
Generate random numbers 6 from 49 ver. 1.0

Instruction:
1. Program generate an output file with result: 'Your_numbers.txt'.
2. Open a file.
3. Numbers always are from the range from 1 to 49.
4. Program returns 8-th lists od numbers from declared range.
5. Each list of numbers is located in separated line, and in brackets.
6. Numbers within the list do not repeat 
   (there is no duplication of results within the list in brackets)
7. Different lists can repeat the same numbers, we always choose numbers from the same range.

Thank You, please open Your result file and press any key to end program.
''')


# Declare a list of numbers to return
list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
                   24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]


# Declare a list
myNumbers_of_8 = []

myNumbers_1 = []
myNumbers_2 = []
myNumbers_3 = []
myNumbers_4 = []
myNumbers_5 = []
myNumbers_6 = []
myNumbers_7 = []
myNumbers_8 = []

# Choice random numbers (1)
for i in range (0, 6):
    n_1 = random.choice(list_of_numbers)
    while n_1 in myNumbers_1:
        n_1 = random.choice(list_of_numbers)
    myNumbers_1.append(n_1)
    myNumbers_1.sort()
myNumbers_of_8.append(myNumbers_1)

# Choice random numbers (2)
for i in range (0, 6):
    n_2 = random.choice(list_of_numbers)
    while n_2 in myNumbers_2:
        n_2 = random.choice(list_of_numbers)
    myNumbers_2.append(n_2)
    myNumbers_2.sort()
myNumbers_of_8.append(myNumbers_2)

# Choice random numbers (3)
for i in range (0, 6):
    n_3 = random.choice(list_of_numbers)
    while n_3 in myNumbers_3:
        n_3 = random.choice(list_of_numbers)
    myNumbers_3.append(n_3)
    myNumbers_3.sort()
myNumbers_of_8.append(myNumbers_3)

# Choice random numbers (4)
for i in range (0, 6):
    n_4 = random.choice(list_of_numbers)
    while n_4 in myNumbers_4:
        n_4 = random.choice(list_of_numbers)
    myNumbers_4.append(n_4)
    myNumbers_4.sort()
myNumbers_of_8.append(myNumbers_4)

# Choice random numbers (5)
for i in range (0, 6):
    n_5 = random.choice(list_of_numbers)
    while n_5 in myNumbers_5:
        n_5 = random.choice(list_of_numbers)
    myNumbers_5.append(n_5)
    myNumbers_5.sort()
myNumbers_of_8.append(myNumbers_5)

# Choice random numbers (6)
for i in range (0, 6):
    n_6 = random.choice(list_of_numbers)
    while n_6 in myNumbers_6:
        n_6 = random.choice(list_of_numbers)
    myNumbers_6.append(n_6)
    myNumbers_6.sort()
myNumbers_of_8.append(myNumbers_6)

# Choice random numbers (7)
for i in range (0, 6):
    n_7 = random.choice(list_of_numbers)
    while n_7 in myNumbers_7:
        n_7 = random.choice(list_of_numbers)
    myNumbers_7.append(n_7)
    myNumbers_7.sort()
myNumbers_of_8.append(myNumbers_7)

# Choice random numbers (8)
for i in range (0, 6):
    n_8 = random.choice(list_of_numbers)
    while n_8 in myNumbers_8:
        n_8 = random.choice(list_of_numbers)
    myNumbers_8.append(n_8)
    myNumbers_8.sort()
myNumbers_of_8.append(myNumbers_8)

# Sort numbers in main list
myNumbers_of_8.sort()

# Define a date of file creation
filename_datetime = datetime.now().strftime("\n\n\tDate: %Y-%m-%d Time: %H:%M:%S")

# Create a output file with your results
sys.stdout = open('Your_numbers.txt', 'w')
print("Your numbers are: \n\n\t", ' \n\t '.join(map(str, myNumbers_of_8[:])))
print(' ')
print('Date and time of creation: ', filename_datetime)
sys.stdout.close()
input()

