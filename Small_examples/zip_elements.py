# zip_elements.py

# I. Equal lists

first_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
seccond_list = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


for items_first_list, items_seccond_list in zip(first_list, seccond_list):
    print(items_first_list, items_seccond_list)


# Not equal list

import itertools

first_list_2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] # 10 elements
seccond_list_2 = [0, 1, 4, 9, 16, 25, 36, 49, 64] # 9 elements

for items_first_list_2, items_seccond_list_2 in itertools.zip_longest(first_list_2, seccond_list_2):
    print(items_first_list_2, items_seccond_list_2) 
