alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encryption(plain_text, shift_key):
    cipher_text=""
    for char in plain_text:
        position = alphabet.index(char)
        new_position = (position + shift_key)%26
        cipher_text += alphabet[new_position]
    print(f"cipher_text is {cipher_text}") 

def decryption(cipher_text,shift_key):
    plain_text=""
    for char in cipher_text:
        position = alphabet.index(char)
        new_position = (position - shift_key)%26
        plain_text += alphabet[new_position]
    print(f"plain_text is {plain_text}")     
    


what_to_do = input("Enter either 'encrypt' or 'decrypt :")
text = input("Enter the plain_text : ")
shift = int(input("Enter the key: "))

if what_to_do == 'encrypt':
    encryption(plain_text=text,shift_key=shift)
else:
    decryption(cipher_text=text,shift_key=shift)    
