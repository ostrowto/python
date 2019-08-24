# frequency.py

import random, sys

input_range = int(input('Please input the frequency range: '))

# face frequency counters
frequency_1 = 0
frequency_2 = 0
frequency_3 = 0
frequency_4 = 0
frequency_5 = 0
frequency_6 = 0
frequency_7 = 0
frequency_8 = 0
frequency_9 = 0
frequency_10 = 0
frequency_11 = 0
frequency_12 = 0
frequency_13 = 0
frequency_14 = 0
frequency_15 = 0
frequency_16 = 0
frequency_17 = 0
frequency_18 = 0
frequency_19 = 0
frequency_20 = 0

# 9 mln die rolls
for roll in range(input_range):
    figure = random.randrange(1, 21)
  
# increment counter
    if figure == 1:
        frequency_1   += 1
    elif figure == 2:
        frequency_2   += 1
    elif figure == 3:
        frequency_3   += 1
    elif figure == 4:
        frequency_4   += 1
    elif figure == 5:
        frequency_5   += 1
    elif figure == 6:
        frequency_6   += 1
    elif figure == 7:
        frequency_7   += 1
    elif figure == 8:
        frequency_8   += 1
    elif figure == 9:
        frequency_9   += 1
    elif figure == 10:
        frequency_10   += 1
    elif figure == 11:
        frequency_11   += 1
    elif figure == 12:
        frequency_12   += 1
    elif figure == 13:
        frequency_13   += 1
    elif figure == 14:
        frequency_14   += 1
    elif figure == 15:
        frequency_15   += 1
    elif figure == 16:
        frequency_16   += 1
    elif figure == 17:
        frequency_17   += 1
    elif figure == 18:
        frequency_18   += 1
    elif figure == 19:
        frequency_19   += 1
    elif figure == 20:
        frequency_20   += 1

sys.stdout = open('freq.txt', 'w') 
print(f'Figure{"Frequency":>13}')
print(f'{1:>4}{frequency_1:>13}')
print(f'{2:>4}{frequency_2:>13}')
print(f'{3:>4}{frequency_3:>13}')
print(f'{4:>4}{frequency_4:>13}')
print(f'{5:>4}{frequency_5:>13}')
print(f'{6:>4}{frequency_6:>13}')
print(f'{7:>4}{frequency_7:>13}')
print(f'{8:>4}{frequency_8:>13}')
print(f'{9:>4}{frequency_9:>13}')
print(f'{10:>4}{frequency_10:>13}')
print(f'{11:>4}{frequency_11:>13}')
print(f'{12:>4}{frequency_12:>13}')
print(f'{13:>4}{frequency_13:>13}')
print(f'{14:>4}{frequency_14:>13}')
print(f'{15:>4}{frequency_15:>13}')
print(f'{16:>4}{frequency_16:>13}')
print(f'{17:>4}{frequency_17:>13}')
print(f'{18:>4}{frequency_18:>13}')
print(f'{19:>4}{frequency_19:>13}')
print(f'{20:>4}{frequency_20:>13}')
sys.stdout.close()