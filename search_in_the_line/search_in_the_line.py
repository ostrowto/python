
# search_in_the_line.py

# info: 
print('''
The program is used to search for the first characters in lines of text files.
Instruction:
1) Enter the file name and press enter.
2) Enter the sentence to search and press enter.
3) Read the result.
4) Press any key to quit program.
''')


# First - input blocks

file_name = input('Enter the file name: ')
searching_term = input('Enter sentence to search: ')

#Seccond - try - except for handle bad file names

try:
    file_hand = open(file_name)
except:
    print('Your file cannot be opened:', file_name)
    quit()

# Third - searching lines

count = 0
for line in file_hand:
    if line.startswith(searching_term):
        count = count + 1
print('There were', count, 'subject lines in file: ', file_name )
input()
