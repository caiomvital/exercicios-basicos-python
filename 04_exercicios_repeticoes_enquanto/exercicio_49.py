# 49) Crie um programa que leia 6 números inteiros e no final mostre quantos deles
# são pares e quantos são ímpares.

numero = 0
contador = 0
contador_pares = 0
contador_impares = 0

while contador < 6:
    numero = int(input("Digite um número:"))
    if numero % 2 == 0:
        contador_pares += 1
    else:
        contador_impares += 1
    contador += 1

print(f"Você digitou {contador_pares} números pares e {contador_impares} números ímpares.")