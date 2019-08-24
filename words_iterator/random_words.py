# random_words.py

import random, sys

results = []

input_your_word_1 = str(input('Input Your word 1: '))
input_your_word_2 = str(input('Input Your word 2: '))
input_your_word_3 = str(input('Input Your word 3: '))
input_your_word_4 = str(input('Input Your word 4: '))
input_your_word_5 = str(input('Input Your word 5: '))

your_range = int(input('Input Your range: '))

results.append(input_your_word_1)
results.append(input_your_word_2)
results.append(input_your_word_3)
results.append(input_your_word_4)
results.append(input_your_word_5)

sys.stdout = open('Your_words.txt', 'w')
for i in range(your_range):
    print(random.choice(results), end = ' ')
sys.stdout.close()