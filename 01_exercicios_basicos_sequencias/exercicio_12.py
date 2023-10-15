# 12) Crie um programa que leia o preço de um produto, calcule e mostre o seu
# PREÇO PROMOCIONAL, com 5% de desconto.

preco = float(input("Digite com o preço do produto: R$ "))
preco_promocional = preco * 0.05
preco_final = preco - preco_promocional

print(f"O preço final do produto é R${preco_final}")