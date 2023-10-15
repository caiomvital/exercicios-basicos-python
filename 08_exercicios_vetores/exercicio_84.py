# 84) Crie um programa que leia o nome e a idade de 9 pessoas e guarde esses
# valores em dois vetores, em posições relacionadas. No final, mostre uma listagem
# contendo apenas os dados das pessoas menores de idade.

tamanho = 9
vetor1 = []
vetor2 = []

for i in range(tamanho):
    vetor1.append(input(f"Digite o nome da pessoa #{i + 1}:"))
    vetor2.append(int(input(f"Digite a idade da pessoa #{i + 1}:")))
for i in range(len(vetor1)):
    if vetor2[i] < 18:
        print(f"{vetor1[i]}, na posição #{i}, é menor de idade com {vetor2[i]} anos.")