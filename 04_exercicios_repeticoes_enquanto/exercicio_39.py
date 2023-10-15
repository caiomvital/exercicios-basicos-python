# 39) Faça um algoritmo que mostre na tela a seguinte contagem:
# 10 9 8 7 6 5 4 3 Acabou!

contador = 10

while contador >= 3:
    print(contador, end=" ")
    contador -= 1
print("Acabou!", end=" ")
