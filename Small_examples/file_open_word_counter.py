# file_open_word_counter.py

from collections import Counter

with open('file.txt') as txt_file:
    wordcount = Counter(txt_file.read().split())


print(len(wordcount))
