# simple_for_else_statement.py

def my_test(my_nums):
    for i in my_nums:
        if i == 0:
            print('There is a zero value!')
            break
    else:
        print('There are no zeros!')

my_test([1, 2, 3, 4, 5, 0])
my_test([1, 2, 3, 4, 5])