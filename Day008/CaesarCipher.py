#CaesarCipher Day008
import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
again = "yes"



def caesar(direction, incoming_text, shift_amount):
    caesar_text = ""
    for letter in incoming_text:
        if letter in alphabet:
            
            position = alphabet.index(letter)
            if direction == "encode":
                new_position = position + shift_amount
                message = "The encoded text is "
            elif direction == "decode":
                new_position = position - shift_amount
                message = "The decoded text is "
            new_letter = alphabet[new_position]
            caesar_text += new_letter
        else:
            caesar_text += letter
    
    print(message + caesar_text)

print(art.logo)

while again == "yes":
    
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    
    caesar(direction, text, shift_amount = shift)
    again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()

print("Goodbye!")
 