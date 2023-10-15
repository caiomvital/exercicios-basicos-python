# 53) Faça um programa que leia a idade e o gênero de 5 pessoas, mostrando no final:
# a) Quantos homens foram cadastrados
# b) Quantas mulheres foram cadastradas
# c) A média de idade do grupo
# d) A média de idade dos homens
# e) Quantas mulheres tem mais de 20 anos

quantidade_homens = 0
quantidade_mulheres = 0
idade = 0
media_idades = 0
media_idades_homens = 0
mulheres_acima_de_20 = 0
soma_idades = 0
soma_idades_homens = 0
contador = 0
while contador < 5:
    genero = input("Digite o gênero: H para homem, M para mulher")
    genero.lower()
    if genero == "h":
        idade = int(input("Digite a idade:"))
        soma_idades += idade
        soma_idades_homens += idade
        quantidade_homens += 1
        contador += 1
    elif genero == "m":
        idade = int(input("Digite a idade:"))
        soma_idades += idade
        quantidade_mulheres += 1
        if idade > 20:
            mulheres_acima_de_20 += 1
        contador += 1
    else:
        print("gênero inválido.")

media_idades = soma_idades / 5
media_idades_homens = soma_idades_homens / quantidade_homens

print(f"Quantidade de Homens cadastrados: {quantidade_homens}.")
print(f"Quantidade de Mulheres cadastradas: {quantidade_mulheres}.")
print(f"Média das idades registradas: {media_idades}.")
print(f"Média de idades dos homens registrados: {media_idades_homens}")
print(f"Quantidade de mulheres acima de 20 anos: {mulheres_acima_de_20}")




