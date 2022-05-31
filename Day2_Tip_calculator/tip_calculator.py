print("Welcome to the Tip Calculator! Bem-vindo à calculadora de gorjetas!")
n=1
language = int(input("Type the number for your language! Digite o número de sua língua!\n1-English\n2-Português\n"))
if (language<1 or language>3):
  print("Error, choose between 1 and 2. Erro,     escolha entre os numeros 1 e 2.")
  language = int(input("Type the number for your language! Digite o número de sua língua! Escriba el número para su idioma\n 1-English\n2-Português\n"))
while n==1:
  if (language==1):
    num_people =int(input("How many people will split the bill?"))
    bill = float(input("What is the total value of the bill? "))
    tip_percentage = int(input("What is the percentage of the tip?"))
    tip = 1+tip_percentage/100
    end_value = round((bill/num_people)*tip ,2)
    print(f"Each person shoul pay {end_value}.")
    n=int(input("\nWould you like to try again?\n1-Yes\n2-No\n"))
  if (language ==2):
    num_people =int(input("Quantas pessoas vão dividir a conta?"))
    bill = float(input("Qual o valor total da conta?"))
    tip_percentage = int(input("Qual é a porcentagem da gorjeta?"))
    tip = 1+tip_percentage/100
    end_value = round((bill/num_people)*tip ,2)
    print(f"Cada pessoa deve pagar {end_value}.")
    n=int(input("\nDeseja tentar novamente?\n1-Sim\n2-Não\n"))
print("\nSee you latter! Até mais tarde!")