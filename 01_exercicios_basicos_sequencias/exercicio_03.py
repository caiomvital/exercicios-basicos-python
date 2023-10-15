#  3) Crie um programa que leia o nome e o salário de um funcionário, mostrando no
# final uma mensagem.
# Ex:
# Nome do Funcionário: Maria do Carmo
# Salário: 1850,45
# O funcionário Maria do Carmo tem um salário de R$1850,45 em Junho.

nome = input("Entre com o nome do funcionário: ")
salario = float(input("Entre com o salário do funcionário: "))

print(f"Nome do Funcionário: {nome}")
print(f"Salário: R$ {salario}")
print(f"O funcionário {nome} tem um salário de R${salario} em Junho.")
