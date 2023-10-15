# 11) Desenvolva uma lógica que leia os valores de A, B e C de uma equação do
# segundo grau e mostre o valor de Delta.

a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))

valor_de_delta = (b ** 2) - (4 * a * c)

print(f"Δ = {valor_de_delta}")
