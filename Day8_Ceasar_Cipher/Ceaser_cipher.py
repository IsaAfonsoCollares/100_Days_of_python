alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def ceasar( inicial_text, shift_num, direction_cipher):
    final_message=""
    for letter in inicial_text:
        if letter in alphabet:
            n=alphabet.index(letter)
            shift = shift_num%26
            if direction_cipher == "encode":
                if n+shift<26:
                    final_message += alphabet[n+shift]
                else:
                    final_message +=alphabet[n+shift-25]
            elif direction_cipher =="decode":
                if n-shift>=0:
                    final_message += alphabet[n-shift]
                else:
                    final_message +=alphabet[n-shift+25]
        else:
            final_message += letter
                
    print(final_message)
should_end = False
language=int(input("Welcome to the Ceaser Cipher! What languafe would you like  to use?\n1-English\n2-Português\n"))
if language ==1:
    while not should_end:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        ceasar(text, shift, direction)
        restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
        if restart == "no":
            should_end = True
            print("Goodbye")
elif language==2:
    while not should_end:
        direction = input("Digite encode para 'codificar' e decode para 'decodificar':\n")
        text = input("Digite sua mensagem:\n").lower()
        shift = int(input("Digite o número de posições:\n"))
        ceasar(text, shift, direction)
        restart = input("Digite yes para utilizar o programa novamente ou no para encerrá-lo.\n")
        if restart == "no":
            should_end = True
            print("Adeus")