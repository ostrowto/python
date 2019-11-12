# sum_and_mul.py

import timeit
print('Sum of squares and sum of the defined range ')
your_range = int(input('Enter your range of numbers: '))

sum_of_numbers = sum(map(lambda i: i + i, range(your_range)))

mul_of_numbers = sum(map(lambda i: i * i, range(your_range)))


print('Simple sum is ', sum_of_numbers)
print('Sum of squares is ', mul_of_numbers)