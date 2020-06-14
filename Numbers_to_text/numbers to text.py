# numbers to text

keysNumbers = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 0: "zero",}

yourNumber = int(input('Your number to text is? '))
toList = [int(x) for x in list(str(yourNumber))]
toKeys = []
for number in range(0, len(toList)):
    toKeys.append(keysNumbers.get(toList[number]))
print(' '.join(toKeys))
print(' \n'.join(toKeys))