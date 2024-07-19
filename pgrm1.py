def cipher(text, shift):
    encrypt_text = ""
    for character in text:
        if character.isalpha():
            shifted = ord(character) + shift
            if character.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif character.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypt_text += chr(shifted)
        else:
            encrypt_text += character
    return encrypt_text

def decipher(text, shift):
    return cipher(text, -shift)

disp = input("Enter the message or text to encrypt: ")
shift_value = int(input("Mention the shift value: "))

encrypted_message = cipher(disp, shift_value)
decrypted_message = decipher(disp, shift_value)

print("The Encrypted message:", encrypted_message)
print("The Decrypted message:", decrypted_message)
