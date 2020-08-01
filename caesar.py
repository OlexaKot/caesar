# Caesar Cipher

# Setup
alphabet = 'abcdefghijklmnopqrstuvwxyz'

# Encryption
def encrypt(plaintext, key):
    ciphertext = ''
    for letter in plaintext:
        if letter.lower() in alphabet:
            is_upper = False
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
        if letter.lower() in alphabet:
            is_upper = False
            if letter not in alphabet:
                is_upper = True
            letter = letter.lower()
            decrypted_letter = alphabet[(alphabet.index(letter) - key) % 26]
            if is_upper == True:
                decrypted_letter = decrypted_letter.upper()
            plaintext += decrypted_letter
        else:
            plaintext += letter
    return plaintext

# Crack
def crack(ciphertext):
    for version in range(0, 26):
        cracked = ''
        for letter in ciphertext:
            if letter.lower() in alphabet:
                is_upper = False
                if letter not in alphabet:
                    is_upper = True
                letter = letter.lower()
                decrypted_letter = alphabet[(alphabet.index(letter) + version) % 26]
                if is_upper == True:
                    decrypted_letter = decrypted_letter.upper()
                cracked += decrypted_letter
            else:
                cracked += letter
        print("+" + str(version) + " " + cracked)
