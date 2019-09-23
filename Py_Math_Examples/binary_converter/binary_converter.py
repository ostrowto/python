# binary_converter.py

input_value = input('Your binary number is: ')

start_number = 0
while input_value != '':
    start_number = start_number * 2 + (ord(input_value[0]) - ord('0'))
    input_value = input_value[1:]

print('Your decimal number is: ', start_number)
