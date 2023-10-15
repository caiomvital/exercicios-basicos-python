# 17) Escreva um programa que pergunte a velocidade de um carro. Caso ultrapasse
# 80Km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba
# o valor da multa, cobrando R$5 por cada Km acima da velocidade permitida.

velocidade = float(input("Digite a velocidade do carro: "))

if velocidade > 80 :
    print("O condutor foi multado. Sua velocidade estava acima de 80km/h!")
    total_multa = (velocidade - 80) * 5
    print(f"A multa foi de R${total_multa}")

