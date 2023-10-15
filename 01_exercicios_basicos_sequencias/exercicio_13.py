# 13) Faça um algoritmo que leia o salário de um funcionário, calcule e mostre o
# seu novo salário, com 15% de aumento.

salario = float(input("Digite o salário do funcionário: R$ "))
novo_salario = salario + (salario * 0.15)

print(f"O novo salário do funcionário será de R$ {novo_salario}")