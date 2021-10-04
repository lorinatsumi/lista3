#1 Escreva um algoritmo que permita a leitura dos nomes de 10 pessoas e armaze os nomes lidos em uma lista. Após isto, o algoritmo deve permitir a leitura de mais 1 nome qualquer de pessoa e depois escrever a mensagem ACHEI, se o nome estiver entre os 10 nomes lidos anteriormente (guardados no vetor), ou NÃO ACHEI caso contrário.

nomes = []

for i in range(10):
  nome=input("Digite um nome: ")
  nomes.append(nome)

print(nomes)

nome1= input("Digite um nome: ")

if nome1 in nomes:
  print("ACHEI")
else:
  print("NÃO ACHEI")



