# prime_2_range.py
import sys


list_of_primes = []

input_to_parameter = int(input('End parameter: '))
end_parameter = input_to_parameter

p = 2

while p <= end_parameter:
    is_prime = True
    for i in range(2, p):
        if p % i == 0:
            is_prime = False
        break
    if is_prime == True:
        list_of_primes.append(p)
        print(p, end = ', ')
    p = p + 1

sys.stdout = open('Your_Prime_Numbers.txt', 'w')
print('\n\nYour prime list is:', list_of_primes)
sys.stdout.close()