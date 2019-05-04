import sys

print('''Program for generating a list of Prime Numbers:
1. Define a lower range
2. Define a upper range
3. Open your file.

Warning! If the upper limit of the test is greater than: 50000, 
         then you will have to wait a long time for the result!
''')

# Define two values
lower_num = int(input('Enter lower range of limit: '))
upper_num = int(input('Enter upper range of limit: '))
print('Please wait... and search your file: Your_Prime_Numbers.txt')

# Init of value and values record to file
total_value = 0
list_of_primes = []

# Simply "for"
for num in range(lower_num, upper_num + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            total_value += num
            list_of_primes.append(num)
    elif num == 2:
        total_value += num
        list_of_primes.append(num)


# Write to file
sys.stdout = open('Your_Prime_Numbers.txt', 'w')
print('The range from which the numbers were generated between: ', lower_num, '-', upper_num)
print ("Sum of prime numbers:", total_value)
print ("Number of generated prime numbers:", len(list_of_primes))
print ("List of prime numbers:\n", list_of_primes)
sys.stdout.close()
