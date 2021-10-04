#1 Escreva um algoritmo que permita a leitura das notas de uma turma de 5 alunos, armazenando os dados numa lista. Depois calcule a média da turma e conte quantos alunos obtiveram nota acima desta média calculada. Escrever a média da turma e o resultado da contagem.

notas =  []

for i in range(5):
  nota=int(input("Digite sua nota: "))
  notas.append(nota)

print (notas) 

soma = 0
for nota in notas:
  soma = (soma + nota)

media = soma / 5
print ("A média da turma é: " + str(media))

