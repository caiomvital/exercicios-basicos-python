# 83) [DESAFIO] Crie uma lógica que preencha um vetor de 20 posições com números
# aleatórios (entre 0 e 99) gerados pelo computador. Logo em seguida, mostre os
# números gerados e depois coloque o vetor em ordem crescente, mostrando no final
# os valores ordenados.
import random

tamanho = 20
vetor = []

for i in range(20):
    vetor.append(random.randint(0, 99))

for i in range(20):
    print(vetor[i], end=" ")
vetor.sort()
print()
for i in range(20):
    print(vetor[i], end=" ")
