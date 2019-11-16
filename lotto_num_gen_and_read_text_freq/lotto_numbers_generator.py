# lotto numbers generator . py

import itertools, collections

file_create = open('numbers_chosen.txt','w')

numbers_to_choose = [1, 2, 3, 4, 5, 6, 7, 8, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]



it = itertools.combinations(numbers_to_choose, 6)



for x in it:
    file_create.write(str(x))
    it = collections.Counter(numbers_to_choose)
    print(x)
    file_create.write('\n')
file_create.close()

