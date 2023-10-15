# 26) Escreva um algoritmo que leia dois números inteiros e compare-os, mostrando
# na tela uma das mensagens abaixo:
#  - O primeiro valor é o maior
#  - O segundo valor é o maior
#  - Não existe valor maior, os dois são iguais

primeiro_numero = int(input("Digite o primeiro número: "))
segundo_numero = int(input("Digite o segundo número: "))

if primeiro_numero > segundo_numero:
    print(f"O primeiro número, {primeiro_numero}, é maior que o segundo número, {segundo_numero}.")
elif segundo_numero > primeiro_numero:
    print(f"O segundo número, {segundo_numero}, é maior que o primeiro número, {primeiro_numero}.")
else:
    print("Os dois números digitados são iguais.")
