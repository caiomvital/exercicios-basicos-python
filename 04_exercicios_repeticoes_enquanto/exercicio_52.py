# 52) Crie um algoritmo que leia a idade de 10 pessoas, mostrando no final:

# a) Qual é a média de idade do grupo
# b) Quantas pessoas tem mais de 18 anos
# c) Quantas pessoas tem menos de 5 anos
# d) Qual foi a maior idade lida

soma = 0
quantidade_maior_18 = 0
quantidade_menor_5 = 0
maior_idade = None
media = 0
contador = 0
idade = 0
while contador < 10:

    idade = int(input(f"Digite a idade número #{contador + 1}:"))
    soma += idade
    if maior_idade is None or idade > maior_idade:
        maior_idade = idade
    if idade > 18:
        quantidade_maior_18 += 1
    if idade < 5:
        quantidade_menor_5 += 1
    contador += 1

media = idade / 10

print(f"A média das idades é {media}.")
print(f"A quantidade de idades acima de 18 anos é {quantidade_maior_18}.")
print(f"A quantidade de idades abaixo de 5 anos é {quantidade_menor_5}.")
print(f"A maior idade lida foi {maior_idade}.")

