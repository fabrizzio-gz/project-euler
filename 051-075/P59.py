"""
A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value, taken from a secret key. The advantage with the XOR function is that using the same encryption key on the cipher text, restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random bytes. The user would keep the encrypted message and the encryption key in different locations, and without both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key. If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message. The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower case characters. Using p059_cipher.txt (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, and the knowledge that the plain text must contain common English words, decrypt the message and find the sum of the ASCII values in the original text.
"""
import itertools
import string

letters = string.ascii_lowercase
# Produce different possible passwords
passwords = itertools.permutations(letters, 3)

with open('p059_cipher.txt') as f:
    text = f.read()
    
chars = text.split(',')
chars = list(map(int, chars))
# Check only first 50 chars
chars = chars[:50]

for key in passwords:
    # Iterates over chars in key
    key_gen = itertools.cycle(key)
    message = ''
    for char in chars:
        message += chr(char^ord(next(key_gen)))
    if 'the' in message:
        print('Current key is:', key)
        print(message)
        print('---------')

#key = ['e', 'x', 'p']


