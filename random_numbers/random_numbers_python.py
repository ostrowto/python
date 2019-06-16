import sys, random

print('''Program for generating one radnom number:
1. Define a lower range
2. Define a upper range
3. Open your file.
''')

lower_num = int(input('Enter lower range of limit: '))
upper_num = int(input('Enter upper range of limit: '))
print('Please search and open your file: Your_Random_Numbers.txt')

start_num = 0
list_of_random_numbers = []

num = random.randrange(lower_num, upper_num+1, 1)

list_of_random_numbers.append(num)
sys.stdout = open('Your_Random_Numbers.txt', 'w')
print('The range from which the numbers were generated between: ', lower_num, '-', upper_num)
print('Your random number is: ', list_of_random_numbers)
