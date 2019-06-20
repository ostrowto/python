# Letter counter

print('The program is used to search for the number of characters in the tested sentence.')


word = input('Put your sentence: ')
searching_l = input('Character for searching: ')

count = 0
for letter in word:
    if letter == searching_l:
        count = count + 1
print(' ')
print('Your search character is: ', searching_l, ' \nand is present in Your sentence: \n', count, ' time/times')
print(' ')
print('For quit program, press any key')
input()