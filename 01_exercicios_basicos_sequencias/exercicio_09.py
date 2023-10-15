# 9) Faça um algoritmo que leia quanto dinheiro uma pessoa tem na carteira (em R$)
# e mostre quantos dólares ela pode comprar. Considere US$1,00 = R$3,45.

valor_em_reais = float(input("Entre com o valor em reais: "))
cotacao = float(input("Entre com a cotação do dólar: "))
valor_em_dolares = valor_em_reais / cotacao
print(f"O valor de R${valor_em_reais} equivale a US${valor_em_dolares}")
