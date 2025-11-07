#found a way to merge both the encrypt and decrypt into a single functon

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
             'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def cipher(word, shift_amount):

    cipher = ""
    for letter in word:
        if direction == 'encode' and letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position + shift_amount) % len(alphabet)
            new_letter = alphabet[new_position]
            cipher += new_letter
        
        elif direction == 'decode' and letter in alphabet:
            position = alphabet.index(letter)           
            new_position = (position - shift_amount) % len(alphabet)
            new_letter = alphabet[new_position]
            cipher += new_letter
        else:
            cipher += letter
    print(cipher)

message = True

while message:
    direction = input("Type 'encode' to encrypt and 'decode' to decrypt: \n")
    text = input("Type your message: \n").lower()
    shift = int(input("Type the shift number: \n"))

    cipher(word = text, shift_amount = shift)
    cipher_more = input("Do you want to cipher more text? Enter 'yes' to continue or 'no' to stop: \n")

    if cipher_more == 'no':
        message = False
        print("Goodbye!!!")