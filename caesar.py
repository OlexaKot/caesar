# Caesar Cipher

# Setup
alphabet = 'abcdefghijklmnopqrstuvwxyz'

# Encryption
def encrypt(plaintext, key):
    ciphertext = ''
    for letter in plaintext:
        is_upper = False
        if letter.lower() in alphabet:
            if letter not in alphabet:
                is_upper = True
            letter = letter.lower()
            encrypted_letter = alphabet[(alphabet.index(letter) + key) % 26]
            if is_upper == True:
                encrypted_letter = encrypted_letter.upper()
            ciphertext += encrypted_letter
        else:
            ciphertext += letter
    return ciphertext

# Decryption
def decrypt(ciphertext, key):
    plaintext = ''
    for letter in ciphertext:
        is_upper = False
        if letter.lower() in alphabet:
            if letter not in alphabet:
                is_upper = True
            letter = letter.lower()
            encrypted_letter = alphabet[(alphabet.index(letter) - key) % 26]
            if is_upper == True:
                encrypted_letter = encrypted_letter.upper()
            plaintext += encrypted_letter
        else:
            plaintext += letter
    return plaintext
