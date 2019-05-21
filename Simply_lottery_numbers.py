import random

myNumbers = []

for i in range (0, 6):
    x = random.randint(1, 50)
    while x in myNumbers:
        x = random.randint(1, 50)
    myNumbers.append(x)

myNumbers.sort()

print("Lottery numbers are: ", (myNumbers))
