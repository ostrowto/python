# enumerate_generator_1.py

my_value = int(input('Your value for generator: '))

def my_generator(any_number):
    my_number = 0
    while my_number < any_number:
        yield my_number
        my_number += 1

for counter_step, my_number in enumerate(my_generator(my_value)):
    print(counter_step, my_number)