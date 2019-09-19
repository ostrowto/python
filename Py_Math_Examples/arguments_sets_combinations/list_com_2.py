# list_com_2.py - pairs of divided numbers by himself

# First set
a_1 = int(input('Your first argument for first set: '))
a_2 = int(input('Your second argument for first set: '))

# Second set
b_1 = int(input('Your first argument for second set: '))
b_2 = int(input('Your second argument for second set: '))



# Numbers divided himself from range defined by user
my_Pairs_2 = [(a, b) for a in range(a_1, a_2) for b in range(b_1, b_2) if a % b == 0 and a != b and b != 1 ]
print(my_Pairs_2)


