# 90) Desenvolva um algoritmo que leia dois valores pelo teclado e passe esses
# valores para um procedimento Somador() que vai calcular e mostrar a soma entre
# eles.

def Somador(a, b):
    print("Resultado da soma:", a + b)

# ----- chamando a função

a = int(input("Digite o primeiro valor:"))
b = int(input("Digite o segundo valor:"))
Somador(a, b)
