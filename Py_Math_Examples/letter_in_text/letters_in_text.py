#letters_in_text.py
letter = open('letter.txt', 'r')
contents = letter.read()
print(contents)
def count_letter(letter, word_list):
    count = 0
    for word in word_list:
        word == word_list
        if letter in word:
            count +- 1
        return count
word_list = []
letter = input('Which letter would you like to count? ')
letter_count = count_letter(letter, word_list)
print('There are: ', letter_count, ' instances of ' + letter)
