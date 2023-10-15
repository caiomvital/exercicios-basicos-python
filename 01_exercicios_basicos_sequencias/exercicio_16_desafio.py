# 16) [DESAFIO] Escreva um programa para calcular a redução do tempo de vida de um
# fumante. Pergunte a quantidade de cigarros fumados por dias e quantos anos ele
# já fumou. Considere que um fumante perde 10 min de vida a cada cigarro. Calcule
# quantos dias de vida um fumante perderá e exiba o total em dias.

cigarros_por_dia = int(input("Digite a quantidade de cigarros por dia"))
anos_em_que_fumou = int(input("Digite quantos anos você fumou"))
minutos_por_cigarro = 10
dias_perdidos = (cigarros_por_dia * minutos_por_cigarro * 365 * anos_em_que_fumou) / (24 * 60)

print(f"O fumante perde um total {dias_perdidos} dias de vida.")