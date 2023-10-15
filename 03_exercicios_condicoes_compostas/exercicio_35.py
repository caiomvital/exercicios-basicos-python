# 35) Uma empresa de aluguel de carros precisa cobrar pelos seus serviços. O
# aluguel de um carro custa R$90 por dia para carro popular e R$150 por dia para
# carro de luxo. Além disso, o cliente paga por Km percorrido. Faça um programa
# que leia o tipo de carro alugado (popular ou luxo), quantos dias de aluguel e
# quantos Km foram percorridos. No final mostre o preço a ser pago de acordo com a
# tabela a seguir:
# - Carros populares (aluguel de R$90 por dia)
#  - Até 100Km percorridos: R$0,20 por Km
#  - Acima de 100Km percorridos: R$0,10 por Km
#  - Carros de luxo (aluguel de R$150 por dia)
#  - Até 200Km percorridos: R$0,30 por Km
#  - Acima de 200Km percorridos: R$0,25 por Km

opcao_carro = int(input("Digite com o tipo de carro escolhido: 1) Popular | 2) Luxo: "))
dias_aluguel = int(input("Digite quantos dias de aluguel: "))
km_percorridos = float(input("Quantos quilômetros foram percorridos? "))
valor_diaria = 0
valor_km = 0
total = 0
tipo_carro = str

if opcao_carro == 1:
    valor_km = 0
    valor_km_total = 0

    if km_percorridos < 100:
        valor_km = 0.20
        valor_km_total = km_percorridos * valor_km
    elif km_percorridos >= 100:
        valor_km = 0.10
        valor_km_total = km_percorridos * valor_km

    valor_diaria = 90
    total = valor_km + (valor_diaria * dias_aluguel)
    tipo_carro = "Popular"

elif opcao_carro == 2:
    valor_km = 0
    valor_km_total = 0

    if km_percorridos < 200:
        valor_km = 0.30
        valor_km_total = km_percorridos * valor_km
    elif km_percorridos >= 200:
        valor_km = 0.25
        valor_km_total = km_percorridos * valor_km

    valor_diaria = 150
    total = valor_km + (valor_diaria * dias_aluguel)
    tipo_carro = "Luxo"

print(f"Tipo de Carro Escolhido: {tipo_carro}.")
print(f"O carro foi alugado por {dias_aluguel} dias.")
print(f"O valor da diária é R${valor_diaria: .2f}.")
print(f"Total de quilômetros percorridos: {km_percorridos}km.")
print(f"O valor por km rodado é R${valor_km: .2f}.")
print(f"O valor total é R${total: .2f}.")




