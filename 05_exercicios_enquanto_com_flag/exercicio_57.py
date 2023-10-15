# 57) Desenvolva um aplicativo que leia o salário e o sexo de vários funcionários.
# No final, mostre o total de salários pagos aos homens e o total pago às
# mulheres. O programa vai perguntar ao usuário se ele quer continuar ou não
# sempre que ler os dados de um funcionário.

salario = 0
genero = 0
total_salarios_h = 0
total_salarios_m = 0
opcao = 0
sair = False
while not sair:
    salario = float(input("Digite o salário do funcionário: R$ "))
    genero = input("Digite o gênero: H para Homem, M para Mulher:")
    genero.lower()
    if genero == "h":
        total_salarios_h += salario
    elif genero == "m":
        total_salarios_m += salario
    opcao = int(input("Deseja continuar? Digite 1 para Sim, 2 para Não: "))
    if opcao == 2:
        sair = True

print(f"Total de Salário pago aos homens: R${total_salarios_h: .2f}")
print(f"Total de salário pago às mulheres: R${total_salarios_m: .2f}")