# 23) Numa promoção exclusiva para o Dia da Mulher, uma loja quer dar descontos
# para todos, mas especialmente para mulheres. Faça um programa que leia nome,
# sexo e o valor das compras do cliente e calcule o preço com desconto. Sabendo
# que:
#  - Homens ganham 5% de desconto
#  - Mulheres ganham 13% de desconto

nome = input("Digite seu nome: ")
genero = input("Digite seu gênero: M para Masculino, F para Feminino ").lower()

if genero == "m":
    print("Gênero Masculino")
    desconto = 0.05
else:
    print("Gênero Feminino")
    desconto = 0.1
valor_das_compras = float(input("Digite o valor total das compras: R$ "))
valor_final = valor_das_compras - (valor_das_compras * desconto)

print(f"O valor final das suas compras será de R$ {valor_final:.2f}!")