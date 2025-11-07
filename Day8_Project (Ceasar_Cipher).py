
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
             'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt and 'decode' to decrypt: \n")
text = input("Type your message: \n").lower()
shift = int(input("Type the shift number: \n"))

def encrypt(word, shift_amount):
    encrypt_text = ""
    
    for letter in word:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position + shift_amount) % len(alphabet)
            new_letter = alphabet[new_position]
            encrypt_text += new_letter

        else:
            encrypt_text += letter

    print(encrypt_text)

def decrypt(word, shift_amount):
    decrypt_text = ""

    for letter in word:
        if letter in alphabet:
            position = alphabet.index(letter)           
            new_position = (position - shift_amount) % len(alphabet)
            new_letter = alphabet[new_position]
            decrypt_text += new_letter
        
        else:
            decrypt_text += letter

    print(decrypt_text)

if direction == 'encode':
    encrypt(word = text, shift_amount = shift)
elif direction == 'decode':
    decrypt(word = text, shift_amount = shift)