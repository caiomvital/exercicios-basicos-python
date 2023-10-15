# 68) Crie um programa que leia sexo e peso de 8 pessoas, usando a estrutura
# “para”. No final, mostre na tela:
# a) Quantas mulheres foram cadastradas
# b) Quantos homens pesam mais de 100Kg
# c) A média de peso entre as mulheres
# d) O maior peso entre os homens

genero = ""
quantidade_mulheres = 0
peso = 0
media_peso_mulheres = 0
soma_pesos_mulheres = 0
homens_acima_100 = 0
maior_peso_homens = float("-inf")

for i in range(0, 8):
    genero = input(f"Digite o gênero da pessoa #{i+1}. (h para homens, m para mulheres): ")
    genero.lower()

    peso = float(input("Digite o peso da pessoa #{i+1}: "))

    if genero == "h" and peso > 100:
        homens_acima_100 += 1
    if genero == "h":
        if maior_peso_homens < peso:
            maior_peso_homens = peso

    if genero == "m":
        quantidade_mulheres += 1
        soma_pesos_mulheres += peso

media_peso_mulheres = soma_pesos_mulheres / quantidade_mulheres

print(f"Quantidade de mulheres: {quantidade_mulheres}.")
print(f"Quantidade de homens acima de 100kg: {homens_acima_100}.")
print(f"Média de peso entre as mulheres: {media_peso_mulheres}")
print(f"Maior peso entre os homens: {maior_peso_homens: .2f}kg.")