#simpleDFibonacci

lastNumber = int(input("Give me a number! "))
index = 1
a, b = 0, 1

while a < lastNumber:
    print(index, a)
    index += 1
    a,b = b, a + b