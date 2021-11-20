#combine.py

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
b = [0 if i < 4 else i for i in a]
print(b)