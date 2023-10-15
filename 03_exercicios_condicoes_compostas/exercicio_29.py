# 29) Desenvolva um programa que leia o nome de um funcionário, seu salário,
# quantos anos ele trabalha na empresa e mostre seu novo salário, reajustado de
# acordo com a tabela a seguir:
#  - Até 3 anos de empresa: aumento de 3%
#  - entre 3 e 10 anos: aumento de 12.5%
#  - 10 anos ou mais: aumento de 20%

nome_funcionario = input("Digite o nome do funcionário: ")
salario = float(input("Digite o salario do funcionario: "))
anos_na_empresa = int(input("Digite a quantidade de anos trabalhados: "))

if anos_na_empresa <= 3:
    salario += (salario * 0.03)
    print(f"Olá, {nome_funcionario}. Você teve um aumento de 3%. Seu novo salário será de: R$ {salario: .2f}")
elif 3 < anos_na_empresa < 10:
    salario += (salario * 0.125)
    print(f"Olá, {nome_funcionario}. Você teve um aumento de 12.5%. Seu novo salário será de: R$ {salario: .2f}")
elif anos_na_empresa > 10:
    salario += (salario * 0.2)
    print(f"Olá, {nome_funcionario}. Você teve um aumento de 20%. Seu novo salário será de: R$ {salario: .2f}")