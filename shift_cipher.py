# Shift cipher

import string

# Get key from user and remove punctuation & duplicate letters
shift_key = raw_input('What is your key?\n')
shift_key = ''.join(letter for letter in list(shift_key) if letter.isalpha())
shift_key = ''.join(sorted(set(shift_key), key=shift_key.index))

# Create lists with regular alphabet
plain_lower = list(string.ascii_lowercase)
plain_upper = list(string.ascii_uppercase)

# Create strings with shifted alphabet
cipher_lower = shift_key.lower() + ''.join(letter for letter in plain_lower if letter not in list(shift_key.lower()))
cipher_upper = shift_key.upper() + ''.join(letter for letter in plain_upper if letter not in list(shift_key.upper()))

# Get text to encrypt
plain_text = raw_input('What phrase do you want to encrypt?\n')
cipher_text = ''

# Perform actual encryption
for i in range(0,len(plain_text)):
    if plain_text[i] in string.ascii_lowercase or plain_text[i] in string.ascii_uppercase: 
        if plain_text[i].islower():
            cipher_text += cipher_lower[plain_lower.index(plain_text[i])]
        else:
            cipher_text += cipher_upper[plain_upper.index(plain_text[i])]
    else:
        cipher_text += plain_text[i]

print "Encoded text: ", cipher_text
