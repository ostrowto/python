# Divide by 3 and 5, 7

input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

def div_by_3(num):
    if num % 3 == 0:
        return True
    else:
        return False

result = (i for i in input_list if div_by_3(i))
print('Divided by 3: ')
print(list(result))

def div_by_5(num):
    if num % 5 == 0:
        return True
    else:
        return False

result = (i for i in input_list if div_by_5(i))
print('Divided by 5: ')
print(list(result))