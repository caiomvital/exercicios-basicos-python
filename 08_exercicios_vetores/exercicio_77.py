# 77) Faça um programa que leia 7 nomes de pessoas e guarde-os em um vetor. No
# final, mostre uma listagem com todos os nomes informados, na ordem inversa
# daquela em que eles foram informados.

tamanho = 7
vetor = []

for i in range(tamanho):
    vetor.append(input(f"Digite o nome da pessoa #{i + 1}:"))
pessoa1 = vetor[0]
vetor.reverse()
for i in range(tamanho):
    if vetor[i] == pessoa1:
        print(vetor[i])
    else:
        print(vetor[i], end=", ")
