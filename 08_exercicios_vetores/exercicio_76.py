# 76) Crie um programa que preencha automaticamente um vetor numérico com 7
# números gerados aleatoriamente pelo computador e depois mostre os valores
# gerados na tela.
import random

vetor = []
for i in range(7):
    valor_aleatorio = random.randint(1, 20)
    vetor.append(valor_aleatorio)
for i in range(7):
    print(vetor[i], end=" ")

