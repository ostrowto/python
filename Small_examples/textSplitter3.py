#textSplitter3


text = input("Please type your text: ")

words = text.split(" ")
sin_words = set(words)

for word in sin_words:
    print(f"'{word}' occurs {words.count(word)} times.")