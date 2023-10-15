# 54) Desenvolva um aplicativo que leia o peso e a altura de 7 pessoas, mostrando
# no final:
# a) Qual foi a média de altura do grupo
# b) Quantas pessoas pesam mais de 90Kg
# c) Quantas pessoas que pesam menos de 50Kg tem menos de 1.60m
# d) Quantas pessoas que medem mais de 1.90m pesam mais de 100Kg.

contador = 0
altura = 0
peso = 0
soma_alturas = 0
media_altura = 0
menos_50_160 = 0
mais_100_190 = 0
mais_90 = 0

while contador < 7:
    altura = float(input(f"digite a altura da pessoa #{contador + 1}:"))
    soma_alturas += altura
    peso = float(input(f"digite o peso da pessoa #{contador + 1}:"))
    if peso > 90:
        mais_90 += 1
    if peso < 50 and altura < 1.6:
        menos_50_160 += 1
    if peso > 100 and altura > 1.9:
        mais_100_190 += 1
    contador += 1

media_altura = soma_alturas / 7

print(f"A média das alturas inseridas é {media_altura: .2f}m.")
print(f"Quantidade de pessoas acima de 90kg: {mais_90}.")
print(f"Quantidade de pessoas abaixo de 50kg e abaixo de 1.6m: {menos_50_160}.")
print(f"Quantidade de pessoas acima de 100kg e acima de 1.9m: {mais_100_190}")
