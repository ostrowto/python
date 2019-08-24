# finf_max_number.py

list_of_numbers = []

number_1 = int(input('Input number 1: '))
number_2 = int(input('Input number 2: '))
number_3 = int(input('Input number 3: '))


def max_number(number_1, number_2, number_3):
    if number_1 >= number_2 and number_1 >= number_3:
        return number_1
    elif number_2 >= number_1 and number_2 >= number_3:
        return number_2
    else:
        return number_3

list_of_numbers.append(number_1)
list_of_numbers.append(number_2)
list_of_numbers.append(number_3)

sorted_list_of_numbers = sorted(list_of_numbers)
print('Your numbers are: ')
print(sorted_list_of_numbers[:])
print('Last number on list is: ')
print(sorted_list_of_numbers[-1])



print('Biggest number is: ')
print(max_number(number_1, number_2, number_3))


