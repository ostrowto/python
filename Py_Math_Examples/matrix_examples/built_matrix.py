# built_matrix.py

import random
from random import randrange

my_Matrix = []
my_Range = int(input('Your range is: '))
for i in range(my_Range):
    my_Matrix.append([])
    for j in range(my_Range):
        my_Matrix[i].append(j)
print(my_Matrix)

my_Matrix_2 = []
my_Range_2 = int(input('Your range is: '))
for i in range(random.randrange(my_Range_2)):
    my_Matrix_2.append([])
    for j in range(random.randrange(my_Range_2)):
        my_Matrix_2[i].append(j)
print(my_Matrix_2)

