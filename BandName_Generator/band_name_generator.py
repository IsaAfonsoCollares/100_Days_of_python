#1. Create a greeting for your program.
print("Hello Human! Olá Humano! Hola Humano")
n=1
language = int(input("Type the number for your language! Digite o número de sua língua! Escriba el número para su idioma\n1-English\n2-Português\n3-Español\n"))
if (language<1 or language>3):
  print("Error, choose between 1, 2 and 3. Erro,     escolha entre os numeros 1, 2 e 3. Error, elige entre los números 1, 2 y 3.  ")
  language = int(input("Type the number for your language! Digite o número de sua língua! Escriba el número para su idioma\n 1-English\n2-Português\n3-Español\n"))
while n==1:
  if (language==1):
    #2. Ask the user for the city that they grew up in.
    city = input("\nWhat city did you grew up in? ")
    #3. Ask the user for the name of a pet.
    pet=input("Tell me the name of one of your pets: ")
    #4. Combine the name of their city and pet and show      them their band name.
    band_name = pet +" " +city
    print("\nYour banda name could be: ", band_name)
    n=int(input("\nWould you like to try again?\n1-Yes\n2-No\n"))
  if (language ==2):
    #2. Pergunte ao usuário a cidade em que ele cresceu.
    city = input("\nEm que cidade você cresceu? ")
    #3. Peça ao usuário o nome de um animal de estimação.
    pet=input("Diga-me o nome de um de seus animais de   estimação: ")
    #4. Combine o nome da cidade e do animal de          estimação e mostre o nome da banda.
    band_name = pet +" " +city
    print("\nSua banda pode se chamar: ", band_name)
    n=int(input("\nDeseja tentar novamente?\n1-Sim\n2-Não\n"))
  if (language ==3):
    #2. Pregúntale al usuario la ciudad en la que creció.
    city = input("\n¿En qué ciudad creciste? ")
    #3. Preguntar al usuario por el nombre de una        mascota.
    pet=input("Dime el nombre de una de tus mascotas: ")
    #4. Haga coincidir la ciudad y el nombre de la       mascota, y muestre el nombre de la banda.
    band_name = pet +" " +city
    print("\nTu banda se puede llamar: ", band_name)
    n=int(input("\n¿Desea volver a intentarlo?\n1-Sí\n2-No\n"))
print("\nSee you latter! Até mais tarde! Hasta la vista!")