# 48) Faça um programa que leia 7 números inteiros e no final mostre o somatório
# entre eles.

contador = 1
numero = 0
soma = 0
while contador <= 7:
    numero = int(input(f"Digite o {contador}º valor:"))
    soma += numero
    contador += 1
print("A soma é ", soma)