# Even and odd numbers search

print('''
Instruction:
1. The program is used to generate even and odd numbers, 
   from the range given by the user.
2. Enter two numbers in the range.
3. Press enter.
4. A result file: "your_result_file.txt" will be generated.
5. Program ends automatically.

''')


import sys

# I. Inputs
input_start_number = int(input('Enter the starting number in the search range: '))
input_end_number = int(input('Enter the end number in the search range: '))

# II. Main calculations
a_numbers = [i for i in range(input_start_number, input_end_number) if i % 2 == 0]
b_numbers = [i for i in range(input_start_number, input_end_number) if i % 2 != 0]

# III. Length of results lists
a_numbers_length = len(a_numbers)
b_numbers_length = len(b_numbers)

# IV. Write results to the file
sys.stdout = open('your_result_file.txt', 'w')

print('Your even numbers are: ', a_numbers)
print(' ')
print('You`ve generated: ', a_numbers_length, 'even numbers from range: ', input_start_number, '-', input_end_number)
print(' ')

print('Your odd numbers are: ', b_numbers)
print(' ')
print('You`ve generated: ', a_numbers_length, 'odd  numbers from range: ', input_start_number, '-', input_end_number)
print(' ')
sys.stdout.close()