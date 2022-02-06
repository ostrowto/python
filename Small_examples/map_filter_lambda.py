# filter_map_lambda.py

x = [1, 2, 3, 4, 5, 6, 7, 21, 2, 22, 3, 45, 566, 1, 0, 2134]

mp_1_filter = filter(lambda i: i % 2 == 0, x)
mp_2_map = map(lambda i: i * 2, x)

print(list(mp_1_filter))
print(list(mp_2_map))