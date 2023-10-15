# 78) Escreva um programa que leia 15 números e guarde-os em um vetor. No final,
# mostre o vetor inteiro na tela e em seguida mostre em que posições foram
# digitados valores que são múltiplos de 10.

tamanho = 15
vetor = []
for i in range(tamanho):
    vetor.append(int(input(f"Digite o valor #{i + 1}:")))

for i in range(tamanho):
    print(vetor[i], end=" ")
print()

for i in range(len(vetor)):
    if vetor[i] % 10 == 0:
        print(vetor[i], f"na posição {i}.")
