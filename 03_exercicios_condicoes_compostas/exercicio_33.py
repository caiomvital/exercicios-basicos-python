# 33) Escreva um programa para aprovar ou não o empréstimo bancário para a compra
# de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e
# em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que
# ela não pode exceder 30% do salário ou então o empréstimo será negado.

valor_casa = float(input("Digite o valor da casa: R$ "))
salario_comprador = float(input("Digite seu salário: R$ "))
anos_emprestimo = int(input("Digite a quantidade de anos em que deseja pagar o empréstimo: "))
meses_emprestimo = anos_emprestimo * 12
prestacao_mensal = valor_casa / meses_emprestimo

if prestacao_mensal > (salario_comprador * 0.3):
    print(f"Empréstimo negado! A parcela mensal de R$ {prestacao_mensal} excede 30% do salário.")
else:
    print(f"Empréstimo aprovado! A parcela mensal será de R$ {prestacao_mensal}.")
