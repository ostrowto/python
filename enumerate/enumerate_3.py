# enumerate_3.py from tuple

my_list = ('el_1', 'el_2', 'el_3', 'el_4', 'el_5', 'el_6','el_7', 'el_8','el_9', 'el_10')

for counter_step, any_element in enumerate(my_list):
    print((counter_step, any_element)*100)
