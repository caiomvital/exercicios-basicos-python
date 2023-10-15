# 59) Crie um programa que leia o genero e a idade de várias pessoas. O programa vai
# perguntar se o usuário quer continuar ou não a cada pessoa. No final, mostre:
# a) qual é a maior idade lida
# b) quantos homens foram cadastrados
# c) qual é a idade da mulher mais jovem
# d) qual é a média de idade entre os homens

genero = 0
idade = 0
opcao = 0
media_idade_homens = 0
quantidade_homens = 0
soma_idade_homens = 0
maior_idade = None
idade_mulher_mais_jovem = None
continuar = True

while continuar:
    genero = input("Digite o gênero: M para Mulher e H para Homem:")
    genero.lower()
    idade = int(input("Digite a idade:"))

    if maior_idade is None or maior_idade < idade:
        maior_idade = idade

    if genero == "m":
        if idade_mulher_mais_jovem is None or idade < idade_mulher_mais_jovem:
            idade_mulher_mais_jovem = idade
    elif genero == "h":
        quantidade_homens += 1
        soma_idade_homens += idade

    opcao = int(input("Deseja continuar? 1 para Sim, 2 para Não:"))
    if opcao == 2:
        continuar = False


print(f"A maior idade inserida foi {maior_idade}.")
print(f"Quantidade de homens cadastrados: {quantidade_homens}.")
print(f"A idade da mulher mais jovem é {idade_mulher_mais_jovem}.")
media_idade_homens = soma_idade_homens / quantidade_homens
print(f"A média de idade entre os homens é {media_idade_homens}.")