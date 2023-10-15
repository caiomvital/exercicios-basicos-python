# 37) Uma empresa precisa reajustar o salário dos seus funcionários, dando um
# aumento de acordo com alguns fatores. Faça um programa que leia o salário atual,
# o gênero do funcionário e há quantos anos esse funcionário trabalha na empresa.
# No final, mostre o seu novo salário, baseado na tabela a seguir:
# - Mulheres
#  - menos de 15 anos de empresa: +5%
#  - de 15 até 20 anos de empresa: +12%
#  - mais de 20 anos de empresa: +23%
# - Homens
#  - menos de 20 anos de empresa: +3%
#  - de 20 até 30 anos de empresa: +13%
#  - mais de 30 anos de empresa: +25%

salario_atual = float(input("Digite o salário atual do funcionário: R$ "))
genero = input("Digite o gênero do funcionário: M - Masculino ou F - Feminino: ")
genero = genero.lower()
anos_de_empresa = int(input("Digite a quantidade de anos em que trabalha na empresa: "))
porcentagem_aumento = 0

if genero == "f":
    if anos_de_empresa < 15:
        porcentagem_aumento = 0.05
    elif 15 <= anos_de_empresa < 20:
        porcentagem_aumento = 0.12
    elif anos_de_empresa >= 20:
        porcentagem_aumento = 0.23
elif genero == "m":
    if anos_de_empresa < 20:
        porcentagem_aumento = 0.03
    elif 20 <= anos_de_empresa < 30:
        porcentagem_aumento = 0.13
    elif anos_de_empresa >= 30:
        porcentagem_aumento = 0.25
else:
    print("gênero inválido")
valor_aumento = salario_atual * porcentagem_aumento
salario_atual = salario_atual + valor_aumento

print(f"Aumento Total: R${valor_aumento: .2f}")
print(f"Salário atual: R${salario_atual: .2f}")
