# 62) Faça um programa usando a estrutura “while True” que leia a idade de
# várias pessoas. A cada laço, você deverá perguntar para o usuário se ele quer ou
# não continuar a digitar dados. No final, quando o usuário decidir parar, mostre
# na tela:
# a) Quantas idades foram digitadas
# b) Qual é a média entre as idades digitadas
# c) Quantas pessoas tem 21 anos ou mais.

idade = 0
soma_idades = 0
quantidade_idades = 0
pessoas_acima_21 = 0

while True:
    idade = int(input("Digite a idade: "))
    quantidade_idades += 1
    soma_idades += idade
    if idade > 21:
        pessoas_acima_21 += 1
    opcao = int(input("Deseja continuar? 1 para Sim, 2 para Não:"))
    if opcao == 2:
        break

media = soma_idades / quantidade_idades
# a) Quantas idades foram digitadas
print(f"Quantidade de idades digitadas: {quantidade_idades}.")
# b) Qual é a média entre as idades digitadas
print(f"Média de idades digitadas: {media}.")
# c) Quantas pessoas tem 21 anos ou mais.
print(f"Quantidade de pessoas acima de 21: {pessoas_acima_21}.")

