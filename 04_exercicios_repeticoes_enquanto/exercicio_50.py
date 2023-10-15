# 50) Desenvolva um programa que faça o sorteio de 20 números entre 0 e 10 e
# mostre na tela:
# a) Quais foram os números sorteados
# b) Quantos números estão acima de 5
# c) Quantos números são divisíveis por 3

import random

contador = 0
acima_de_5 = 0
divisiveis_por_3 = 0
numero = 0
print("Números Sorteados:", end=" ")
while contador < 20:
    numero = random.randint(0, 10)
    print(numero, end=" ")
    if numero % 3 == 0:
        divisiveis_por_3 += 1
    if numero > 5:
        acima_de_5 += 1
    contador += 1
print(f"\nQuantidade de números acima de 5: {acima_de_5}")
print(f"Quantidade de números divisíveis por 3: {divisiveis_por_3}")
