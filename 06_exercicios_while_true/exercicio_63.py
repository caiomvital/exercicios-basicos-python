# 63) Crie um programa usando a estrutura “while True” que leia vários números.
# A cada laço, pergunte se o usuário quer continuar ou não. No final, mostre na
# tela:
# a) O somatório entre todos os valores
# b) Qual foi o menor valor digitado
# c) A média entre todos os valores
# d) Quantos valores são pares

menor_valor = None
quantidade_valores = 0
quantidade_pares = 0
soma = 0
while True:

    valor = int(input("Digite um valor: "))
    soma += valor
    quantidade_valores += 1

    if menor_valor is None or valor < menor_valor:
        menor_valor = valor

    if valor % 2 == 0:
        quantidade_pares += 1

    opcao = int(input("Deseja continuar? 1 para Sim, 2 para Não: "))
    if opcao == 2:
        break

media = soma / quantidade_valores

# a) O somatório entre todos os valores
print(soma)
# b) Qual foi o menor valor digitado
print(menor_valor)
# c) A média entre todos os valores
print(media)
# d) Quantos valores são pares
print(quantidade_pares)