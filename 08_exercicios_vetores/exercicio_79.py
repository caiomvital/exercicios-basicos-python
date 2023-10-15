# 79) Desenvolva um programa que leia 10 números inteiros e guarde-os em um vetor.
# No final, mostre quais são os números pares que foram digitados e em que
# posições eles estão armazenados.

tamanho = 10
vetor = []

for i in range(tamanho):
    vetor.append(int(input(f"Digite um valor para a posição #{i} do vetor: ")))

for i in range(len(vetor)):
    if vetor[i] % 2 == 0:
        print(vetor[i], end=" ")
        print(f"na posição {i}.")