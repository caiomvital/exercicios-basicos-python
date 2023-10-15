# 34) O Índice de Massa Corpórea (IMC) é um valor calculado baseado na altura e no
# peso de uma pessoa. De acordo com o valor do IMC, podemos classificar o
# indivíduo dentro de certas faixas.
#  - abaixo de 18.5: Abaixo do peso
#  - entre 18.5 e 25: Peso ideal
#  - entre 25 e 30: Sobrepeso
#  - entre 30 e 40: Obesidade
#  - acima de 40: Obseidade mórbida
# Obs: O IMC é calculado pela expressão peso/altura² (peso dividido pelo quadrado
# da altura)

altura = float(input("Digite sua altura em m"))
peso = float(input("Digite seu peso em kg"))
imc = peso / (altura ** 2)

print(f"Seu IMC está em {imc: .2f}.")

if imc < 18.5:
    print("Abaixo do peso")
elif 18.5 <= imc <= 25:
    print("Peso ideal")
elif 25 < imc < 30:
    print("Sobrepeso")
elif 30 <= imc <= 40:
    print("Obesidade")
elif imc >= 40:
    print("Obesidade mórbida")
