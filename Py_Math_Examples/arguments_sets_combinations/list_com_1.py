# list_com_1.py - combination of 9 arguments in 3 sets

# First set
a_1 = int(input('Your first argument for first set: '))
a_2 = int(input('Your second argument for first set: '))
a_3 = int(input('Your third argument for first set: '))

# Second set
b_1 = int(input('Your first argument for second set: '))
b_2 = int(input('Your second argument for second set: '))
b_3 = int(input('Your third argument for second set: '))

# Third set
c_1 = int(input('Your first argument for third set: '))
c_2 = int(input('Your second argument for third set: '))
c_3 = int(input('Your third argument for third set: '))


my_Pairs_1 = [(a, b, c) for a in (a_1, a_2, a_3) for b in (b_1, b_2, b_3) for c in (c_1, c_2, c_3)]
print(my_Pairs_1)

