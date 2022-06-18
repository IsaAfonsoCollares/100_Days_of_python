from random import choice
from hangman_art import logo, layout
print(logo)
n=1
language = int(input("Choose you language:\n1-Português\n2-English\n"))
if language == 1:
#versão português
    while n==1:
        from palavras import lista
        level=int(input("Escolha o nível de dificuldade:\n1-Fácil\n2-Médio\n3-Difícil\n4-Impossível\n"))
        opcao = lista[level-1]
        palavra= choice(opcao)
        n= len(palavra)
        space = []
        for i in range(0,n):
            space.append("_ ")
        print('-'.join(map(str, space)))
        print(f"A palavra tem {n} letras")
        vidas=5
        while vidas>0:
            for i in range (0, n):
                letra=input(f"Letra: ")
                if letra in palavra:
                    ind = palavra.index(letra)
                    space[ind] = letra
                else:
                    vidas-=1      
                print(layout[5])
                print('-'.join(map(str, space)))
        if vidas==0:
            print("\nVOCÊ PERDEU")
            print(f"A palavra é: {palavra}")
        else:
            print("\nVOCÊ GANHOU")
        n=int(input("\nJogar novamente?:\n1-Sim\n2-Não\n"))
print("Thanks for playing!\nObrigado por jogar!")