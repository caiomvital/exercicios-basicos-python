# 60) Desenvolva um algoritmo que leia o nome, a idade e o sexo de várias pessoas.
# O programa vai perguntar se o usuário quer ou não continuar. No final, mostre:
# a) O nome da pessoa mais velha
# b) O nome da mulher mais jovem
# c) A média de idade do grupo
# d) Quantos homens tem mais de 30 anos
# e) Quantas mulheres tem menos de 18 anos

quantidade_pessoas = 0
maior_idade = 0
nome_pessoa_mais_velha = ""
idade_mulher_mais_jovem = None
nome_mulher_mais_jovem = ""
soma_idades = 0
homens_acima_30 = 0
mulheres_abaixo_18 = 0
media_idades = 0

while True:

    nome = input("Digite o nome da pessoa:")
    idade = int(input("Digite a idade da pessoa:"))
    genero = input("Digite o gênero (h para homem, m para mulher")
    genero.lower()

    soma_idades += idade
    quantidade_pessoas += 1

    if maior_idade < idade:
        maior_idade = idade
        nome_pessoa_mais_velha = nome

    if genero == "h" and idade > 30:
        homens_acima_30 += 1

    if genero == "m":
        if idade < 18:
            mulheres_abaixo_18 += 1
        if idade_mulher_mais_jovem is None or idade < idade_mulher_mais_jovem:
            idade_mulher_mais_jovem = idade
            nome_mulher_mais_jovem = nome

    continuar = input("Deseja continuar? S para Sim, N para Não: ")
    continuar.lower()

    if continuar != "s":
        break

    if quantidade_pessoas > 0:
        media_idades = soma_idades / quantidade_pessoas

print(f"O nome da pessoa mais velha é {nome_pessoa_mais_velha}.")
print(f"O nome da mulher mais jovem é {nome_mulher_mais_jovem}.")
print(f"A média de idades é {media_idades}.")
print(f"A quantidade de homens acima de 30 é {homens_acima_30}.")
print(f"A quantidade de mulheres abaixo dos 18 anos é {mulheres_abaixo_18}.")