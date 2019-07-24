# this is simple guess the number text game.

import random

print('*******************************************')
print('* Welcome in simply guess the number game *')
print('* Instrucion:                             *')
print('* 1) Define Your range of numbers         *')
print('* 2) Declare how many times You want      *')
print('*    to guess                             *')
print('*******************************************')





first_number = input('The smallest possible number? ')
first_number_int = int(first_number)

seccond_number = input('The largest possible number? ')
seccond_number_int = int(seccond_number)


secret_Number = random.randint(first_number_int, seccond_number_int)

print('We thinking of a number between ' + str(first_number_int) + ' and ' + str(seccond_number_int))



guess_number_higher = input('How many times do you want to guess? ')
guess_number_higher_int = int(guess_number_higher)
guess_number_higher_int_plus_one = guess_number_higher_int + 1


for guessesTaken in range(1, guess_number_higher_int_plus_one):
    print('Please think about numbers from Your range of numbers and take a guess... ')
    guess = int(input())

    if guess < secret_Number:
        print('Your guess is to low! Try again')
    elif guess > secret_Number:
        print('Your guess is to high! Try again')
    else:
        break

if guess == secret_Number:
    print('You guessed the secret number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Sorry! You`ve guessed ', guess_number_higher_int, ' (times). The secret number was: ' + str(secret_Number))

print('Please press any key to end the game')
input()
