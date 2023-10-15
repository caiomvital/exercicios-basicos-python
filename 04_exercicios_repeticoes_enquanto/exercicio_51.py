# 51) Faça um aplicativo que leia o preço de 8 produtos. No final, mostre na tela
# qual foi o maior e qual foi o menor preço digitados.

preco = 0
contador = 0
maior_preco = float('-inf')
menor_preco = float('inf')

while contador < 8:
    preco = float(input(f"Digite o {contador + 1}º preço: "))
    if preco > maior_preco:
        maior_preco = preco
    if preco < menor_preco:
        menor_preco = preco
    contador += 1
print(f"O maior preço foi R${maior_preco}")
print(f"O menor preço foi R${menor_preco}")
