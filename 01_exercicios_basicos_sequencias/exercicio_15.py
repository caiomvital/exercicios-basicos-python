# 15) Crie um programa que leia o número de dias trabalhados em um mês e mostre o
# salário de um funcionário, sabendo que ele trabalha 8 horas por dia e ganha R$25
# por hora trabalhada.

dias_trabalhados = int(input("Entre com a quantidade de dias trabalhados: "))
horas_totais = 8 * dias_trabalhados
salario = horas_totais * 25

print(f"O salário do funcionário no mês foi de R${salario}")