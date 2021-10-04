#Faça um algoritmo para ler 5 números e armazenar em uma lista. Após a leitura, o algoritmo deve escrever esses 5 números lidos na ordem inversa.

numeros = []

for i in range(5):
  numero=input("Digite um numero: ")
  numeros.append(numero)

print (numeros)

print (str(numeros[4]) + str(numeros[3]) + str(numeros[2]) + str(numeros[1]) + str(numeros[0]))