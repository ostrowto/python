# multiplication_table.py

number_to_multiplication = int(input('Input Your number to multiplication: '))

how_many = int(input('How many computations: '))
how_many_computations = how_many + 1


for any_item in range(1, how_many_computations):
    print(number_to_multiplication, 'x', any_item, '=', number_to_multiplication * any_item)