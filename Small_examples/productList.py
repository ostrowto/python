# productList.py

steps_on_list = int(input('How many steps do You want? '))

product_Id_List = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
product_added_list = []
index = 0

while (index < 10):
    print('You`re on this step on list: ', product_Id_List[index])
    index += 1
    product_added_list.append(index)
    if product_Id_List[index] == steps_on_list:
        break
    else:
        print('Hurra', product_added_list)