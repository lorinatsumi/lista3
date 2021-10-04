#Faça um algoritmo para ler uma lista de 5 números. Após isto, ler mais um número qualquer, calcular e escrever quantas vezes esse número aparece na lista.


numeros = []

for i in range(5):
  numero=input("Digite um numero: ")
  numeros.append(numero)

num = input("Digite um numero qualquer: ")

print(numeros)

quant = numeros.count(num)


print (f"O valor {num} aparece {quant} vezes na lista")