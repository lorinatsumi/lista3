#Leia 5 números em uma lista. A seguir encontre o maior número digitado, apresentando para o usuário este número e a posição que ele se encontra na lista.


numeros = []

for i in range(5):
  numero=input("Digite um numero: ")
  numeros.append(numero)

indice = 0
maior = numeros[0]

for i in range(5):
  if maior < numeros[i]:
    maior = numeros [i]
    indice = i


print ("O maior número é: " + str(maior))
print (f"Está na posição: {indice}")