def encode(alphabet, text, shift):
    final_message=[]
    message=list(text)
    for letter in message:
        n=alphabet.index(letter)
        if n+shift<=26:
            new_letter=alphabet[n+shift]
            final_message.append(new_letter)
        else:
            new_letter=alphabet[26-shift]
            final_message.append(new_letter)
    return final_message
def decode(alphabet, text, shift):
    final_message=[]
    message=list(text)
    for letter in message:
        n=alphabet.index(letter)
        if n-shift>=0:
            new_letter=alphabet[n-shift]
            final_message.append(new_letter)
        else:
            new_letter=alphabet[-shift]
            final_message.append(new_letter)
    return final_message
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
if direction == 'encode':
    final_text=encode(alphabet, text, shift)
elif direction == 'decode':
    final_text=decode(alphabet, text, shift)
print(''.join(map(str, final_text)))