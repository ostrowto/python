# enumerate_string_1.py

your_string = str(input('Your string is: '))

for my_item, letter_in_string in enumerate(your_string, start = 1):
    print(letter_in_string, 'is', my_item, '-th letter in text: ', '>', your_string, '<')

