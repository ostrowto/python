from random import randrange

parameter1 = int(input("Param 1: - list minimum "))
parameter2 = int(input("Param 2: - list maximum "))
parameter3 = int(input("Param 3: - how many do you want?"))

myList = [randrange(parameter1, parameter2) for i in range(parameter3)]
print(sorted(myList, key=lambda x: x ** 2))

