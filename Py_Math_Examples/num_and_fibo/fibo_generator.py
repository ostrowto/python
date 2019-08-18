#fibo_generator.py

import sys

fibo_list = []
a,b = 1, 1
sys.stdout = open('Your_fibo.txt', 'w')
for c in range(1, 10000):
    print(a)
    n = a + b
    a = b
    b = n
print(list)
sys.stdout.close() 
