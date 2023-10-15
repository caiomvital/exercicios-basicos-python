# 42) Faça um algoritmo que pergunte ao usuário um número inteiro e positivo
# qualquer e mostre uma contagem até esse valor:
# Ex: Digite um valor: 35
# Contagem: 1 2 3 4 5 6 7 ... 33 34 35 Acabou!

numero = int(input("Digite um número inteiro: "))
contador = 1

print("Contagem:", end=" ")
while contador <= numero:
    print(contador, end=" ")
    contador += 1
print("Acabou!")