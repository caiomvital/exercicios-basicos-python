# 10) Faça um algoritmo que leia a largura e altura de uma parede, calcule e
# mostre a área a ser pintada e a quantidade de tinta necessária para o serviço,
# sabendo que cada litro de tinta pinta uma área de 2metros quadrados.

largura = int(input("Entre com a largura da parede: "))
altura = int(input("Entre com a altura da parede: "))
area = largura * altura
litros_tinta = area / 2
print(f"A área total da parede é de {area}m².")
print(f"A quantidade de tinta necessária é {litros_tinta} litros.")