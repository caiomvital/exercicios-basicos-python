# 72) Crie um programa que preencha automaticamente (usando lógica, não apenas
# atribuindo diretamente) um vetor numérico com 10 posições, conforme abaixo:
# 5 10 15 20 25 30 35 40 45 50
# 0 1 2 3 4 5 6 7 8 9

tamanho = 10
vetor1 = []

for i in range(tamanho):
    valor = (i +1) * 5
    vetor1.append(valor)

for i in range(tamanho):
    print(vetor1[i], end=" ")
print()
for i in range (tamanho):
    print(i, end="  ")


