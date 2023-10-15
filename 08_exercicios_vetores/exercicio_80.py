# 80) Faça um algoritmo que preencha um vetor de 30 posições com números entre 1 e
# 15 sorteados pelo computador. Depois disso, peça para o usuário digitar um
# número (chave) e seu programa deve mostrar em que posições essa chave foi
# encontrada. Mostre também quantas vezes a chave foi sorteada.
import random

tamanho = 30
vetor = []
valor = 0
quantidade_sorteio = 0
for i in range(tamanho):
    valor = random.randint(1, 15)
    vetor.append(valor)
valor_digitado = int(input("Digite um valor:"))

for i in range(len(vetor)):
    if vetor[i] == valor_digitado:
        print(f"Valor encontrado na posição #{i} do vetor.")
        quantidade_sorteio += 1
print(f"A chave foi sorteada {quantidade_sorteio} vezes.")

