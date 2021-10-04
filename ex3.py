#Leia 5 números em uma lista. A seguir encontre o maior número digitado, apresentando para o usuário este número e a posição que ele se encontra na lista.


numeros = []

for i in range(5):
  numero=input("Digite um numero: ")
  numeros.append(numero)


maior = numeros[0]

if maior < numeros[1]:
  maior = numeros [1]

if maior < numeros[2]:
  maior = numeros[2]

if maior < numeros[3]:
  maior = numeros[3]

if maior < numeros[4]:
  maior = numeros[4]

print ("O maior número é: " + str(maior))