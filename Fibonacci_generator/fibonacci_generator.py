# Fibonacci generator

import sys

input_your_range = input('Your range is: ')
n = int(input_your_range)
def fib(n):
    a = 0
    b = 1
    while a < n:
        print(a, end = ' ')
        a, b = b, a + b
    print()
fib(n)


sys.stdout = open('Your_Fibonacci_Numbers.txt', 'w')
print('Your Fibonacci Numbers: ')
fib(n)
sys.stdout.close()

print('Press any key to end and open file with generated Fibonacci numbers')
input()