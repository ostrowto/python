# multiplication_table_2.py



start_num = int(input('Start number for multiplications: '))
end_num_to_calc = int(input('End number for multiplications: '))
end_num = end_num_to_calc + 1


print('\t\t\t   multiplication_table_2.py\n')

for i in range(start_num, end_num):
    print(i, end = '\t')
print()
print('_' * 120)

for j in range(start_num, end_num):
    for k in range(start_num, end_num):
        print(j * k, end = '\t')
    print('\n')