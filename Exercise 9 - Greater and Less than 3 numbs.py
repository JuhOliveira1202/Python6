#Exercício 9:
#Elabora um programa que calcule o maior e menor de 3 números.
#Dica1: comparar 2 a 2
#Dica2: ou comparar os 3 usando o and

numero1 = int (input("intruduza um número"))
numero2 = int (input("intruduza um número"))
numero3 = int (input("intruduza um número"))

if numero1>numero2>numero3:
    print("O número", numero1, "é maior que o numéro", numero2, "e que o número", numero3)

elif numero1 == numero2 == numero3:
    print("Os números são todos iguais")

elif numero1<numero2>numero3:
    print("O número", numero1, "é menor que o número", numero2, "e" , numero2 , " é maior que o número", numero3)

elif numero1>numero2<numero3:
    print("O número", numero1, "é maior que o número", numero2, "e" , numero2 , " é menor que o número", numero3)

elif numero1<numero2<numero3:
    print("O número", numero1, "é menor que o número", numero2, "e menor que o número", numero3)

else:
    print("condição não pensada, contacte o administrador!")
