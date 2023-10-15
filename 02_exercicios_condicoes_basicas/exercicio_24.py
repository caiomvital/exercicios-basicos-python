# 24) Faça um algoritmo que pergunte a distância que um passageiro deseja
# percorrer em Km. Calcule o preço da passagem, cobrando R$0.50 por Km para
# viagens até 200Km e R$0.45 para viagens mais longas.

distancia = float(input("Digite a distância a ser percorrida: "))
valor_cobrado = 0

if distancia <= 200:
    valor_cobrado = 0.50
else:
    valor_cobrado = 0.45

total = distancia * valor_cobrado

print(f"O valor a ser cobrado pela distância de {distancia}km será de R${total:.2f}.")