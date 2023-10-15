# 85) Faça um algoritmo que leia o nome, o gênero e o salário de 5 funcionários e
# guarde esses dados em três vetores. No final, mostre uma listagem contendo
# apenas os dados das funcionárias mulheres que ganham mais de R$5 mil.

tamanho = 5
vetor_nomes = []
vetor_generos = []
vetor_salarios = []

for i in range(tamanho):
    vetor_nomes.append(input("Digite o nome do funcionário: "))
    vetor_generos.append(input("Digite o gênero do funcionário (h para homem, m para mulher): "))
    vetor_generos[i].lower()
    vetor_salarios.append(float(input("Digite o salário do funcionário: R$")))

for i in range(tamanho):
    if vetor_generos[i] == "m" and vetor_salarios[i] > 5000:
        print(f"{vetor_nomes[i]} ganha R$ {vetor_salarios[i]}.")
