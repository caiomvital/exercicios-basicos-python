# 91) Desenvolva um algoritmo que leia dois valores pelo teclado e passe esses
# valores para um procedimento Maior() que vai verificar qual deles é o maior e
# mostrá-lo na tela. Caso os dois valores sejam iguais, mostrar uma mensagem
# informando essa característica.

def Maior(a, b):
    if a > b:
        print(f"{a} é maior que {b}.")
    elif a < b:
        print(f"{a} é menor que {b}.")
    else:
        print(f"{a} e {b} são iguais.")

# ---- chamando a função
a = int(input("Digite o primeiro valor:"))

b = int(input("Digite o segundo valor:"))

Maior(a, b)
