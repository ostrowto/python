# searching_in_list.py

my_List = ['item_1', 'item_2', 'item_3', 'item_4', 'item_5']

my_List_Select = ''

while str.upper(my_List_Select) != 'QUIT':
    my_List_Select = input('Please input a element name: ')
    if (my_List.count(my_List_Select) >= 1):
        print('This element exist ')
    elif (str.upper(my_List_Select) != 'QUIT'):
        print('The list doesn`t contain this element')
