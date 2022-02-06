#kostka.py

import random
import time

input_your_number = input("Please input your number: ")
input_your_number_int = int(input_your_number)

first_roll = random.randint(1, 6)
seccond_roll = random.randint(1, 6)
third_roll = random.randint(1, 6)
four_roll = random.randint(1, 6)
five_roll = random.randint(1, 6)
six_roll = random.randint(1, 6)

if first_roll == input_your_number_int:
    print(f'"Great You win! Your number is: " {input_your_number_int}, " Computer roll result was: {first_roll} as first roll"')
elif seccond_roll == input_your_number_int:
    print(f'"Great You win! Your number is: " {input_your_number_int}, " Computer roll result was: {seccond_roll} as seccond roll"')
elif third_roll == input_your_number_int:
    print(f'"Great You win! Your number is: " {input_your_number_int}, " Computer roll result was: {third_roll} as third roll"')
elif four_roll == input_your_number_int:
    print(f'"Great You win! Your number is: " {input_your_number_int}, " Computer roll result was: {four_roll} as four roll"')
elif five_roll == input_your_number_int:
    print(f'"Great You win! Your number is: " {input_your_number_int}, " Computer roll result was: {five_roll} as five roll"')
elif six_roll == input_your_number_int:
    print(f'"Great You win! Your number is: " {input_your_number_int}, " Computer roll result was: {six_roll} as six roll"')
else:
    print(f'"Sorry, you`ve lost!" , "Your number was: {input_your_number_int}", "Computer roll result was: {first_roll}, {seccond_roll}, {third_roll}, {four_roll}, {five_roll}, {six_roll}"')
time.sleep(5)
