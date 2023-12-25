import init

def cipher_key():
    cipher_key=None
    for i in range(len(init.load_key().decode())):
        if init.load_key().decode()[i].isnumeric():
            cipher_key=init.load_key().decode()[i]
            break
    return cipher_key

def cipher(plaintext):
    key=int(cipher_key())
    ciphertext = ""
    for letter in plaintext:
        if letter.isalpha():
            if letter.isupper():
                ciphertext += chr((ord(letter) - ord('A') + key) % 26 + ord('A'))
            else:
                ciphertext += chr((ord(letter) - ord('a') + key) % 26 + ord('a'))
        else:
            ciphertext += letter
    to_add=init.load_key().decode()
    ciphertext+=to_add
    return ciphertext

def decipher(ciphertext):
    key=int(cipher_key())
    temp=init.load_key().decode()
    ciphertext=ciphertext.replace(temp,"")
    plaintext = ""
    for letter in ciphertext:
        if letter.isalpha():
            if letter.isupper():
                plaintext += chr((ord(letter) - ord('A') - key) % 26 + ord('A'))
            else:
                plaintext += chr((ord(letter) - ord('a') - key) % 26 + ord('a'))
        else:
            plaintext += letter
    return plaintext