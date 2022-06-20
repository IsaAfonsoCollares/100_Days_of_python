from random import choice
from hangman_art import logo, layout
from palavras import lista


def word_choice(level):
    opcao = lista[level-1]
    word= list(choice(opcao))
    return(word)

def letter_in_word (guess, word):
    ind=0
    for letter in word:
        ind +=1
        if guess==letter:
           space[ind-1]=guess
    return (space)

print(logo)
n=1
language = int(input("Choose you language:\n1-Português\n2-English\n"))
if language == 1:
#versão português
    while n==1:
        from palavras import lista
        level=int(input("Escolha o nível de dificuldade:\n1-Fácil\n2-Médio\n3-Difícil\n4-Impossível\n"))
        palavra = word_choice(level)
        letter_guessed =[]
        space=[]
        for i in range(0,len(palavra)):
            space.append("_ ")
        print(f"A palavra tem {len(palavra)} letras")
        print('-'.join(map(str, space)))
        print(layout[0])
        error_num = 0
        while error_num<6:
            guess=input(f"Letra: ")
            letter_guessed.append(guess)
            if guess in palavra:
                space=letter_in_word(guess, palavra)
            elif guess not in palavra:
                error_num +=1
                print(f"Erros: {error_num}")
            print(f"Letras: {' '.join(map(str, letter_guessed))}")        
            print(layout[error_num])
            print(f"Palavra:{'-'.join(map(str, space))}")
            if space==palavra:
                break
        if error_num==6:
            print("\nVOCÊ PERDEU")
            print(f"A palavra é: {''.join(map(str, palavra))}")
        else:
            print("\nVOCÊ GANHOU")
        n=int(input("\nJogar novamente?:\n1-Sim\n2-Não\n"))
if language ==2:
    while n==1:
        from palavras import lista
        level=4
        palavra = word_choice(level)
        letter_guessed =[]
        space=[]
        for i in range(0,len(palavra)):
            space.append("_ ")
        print(f"The word has {len(palavra)} letters")
        print('-'.join(map(str, space)))
        print(layout[0])
        error_num = 0
        while error_num<6:
            guess=input(f"Letter: ")
            letter_guessed.append(guess)
            if guess in palavra:
                space=letter_in_word(guess, palavra)
            elif guess not in palavra:
                error_num +=1
                print(f"Errors: {error_num}")
            print(f"Guesses: {' '.join(map(str, letter_guessed))}")        
            print(layout[error_num])
            print(f"Word:{'-'.join(map(str, space))}")
            if space==palavra:
                break
        if error_num==6:
            print("\nYOU LOST")
            print(f"THE WORD IS: {''.join(map(str, palavra))}")
        else:
            print("\nYOU WON!")
        n=int(input("\nWOULD YOU LIKE TO PLAY AGAIN?:\n1-YES\n2-NO\n"))
print("Thanks for playing!\nObrigado por jogar!")