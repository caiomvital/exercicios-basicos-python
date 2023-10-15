# 61) Crie um programa que mostre na tela a seguinte contagem, usando a estrutura
# “while True”
# 0 3 6 9 12 15 18 21 24 27 30 Acabou!

contador = 0
while True:
    print(contador, end=" ")
    contador += 3

    if contador > 30:
        break

print("Acabou!")