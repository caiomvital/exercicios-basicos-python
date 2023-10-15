# 14) A locadora de carros precisa da sua ajuda para cobrar seus serviços. Escreva
# um programa que pergunte a quantidade de Km percorridos por um carro alugado e a
# quantidade de dias pelos quais ele foi alugado. Calcule o preço total a pagar,
# sabendo que o carro custa R$90 por dia e R$0,20 por Km rodado.

quantidade_de_km = float(input("Digite a quantidade de quilômetros percorridos: "))
quantidade_de_dias = int(input("Entre com a quantidade de dias de aluguel: "))
valor_carro_por_dia = 90
valor_km = 0.20
valor_do_aluguel = valor_carro_por_dia * quantidade_de_dias
valor_da_kilometragem = valor_km * quantidade_de_km
valor_final = valor_do_aluguel + valor_da_kilometragem

print(f"fO carro foi alugado por {quantidade_de_dias}. A diária custa R$ {valor_carro_por_dia}")
print(f"A quantidade de km rodados foi de {quantidade_de_km}km. O valor por km é de R${valor_km}")
print(f"O valor total do aluguel foi de R$ {valor_do_aluguel}")
print(f"O valor total da quilometragem é de R$ {valor_da_kilometragem}")
print(f"O valor final a ser cobrado é de R${valor_final}")

