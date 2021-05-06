#cesar.py

print('Input your message ')
YourInputMessage = input()

print('Input your decryption key')
YourDecryptionKey = int(input())

YourDecryptedMessage = ''

for x in YourInputMessage:
    YourNumber = ord(x)
    YourNumber += YourDecryptionKey
    YourDecryptedMessage += chr(YourNumber)

print('Your decrypted message is: ')
print(YourDecryptedMessage)