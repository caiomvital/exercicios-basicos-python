# 41) Desenvolva um programa que mostre na tela a seguinte contagem:
# 100 95 90 85 80 ... 0 Acabou!

contador = 100

while contador >= 0:
    print(contador, end=" ")
    contador -= 5
print("Acabou!")