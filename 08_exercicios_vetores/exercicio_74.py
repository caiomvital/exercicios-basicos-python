# 74) Crie um programa que preencha automaticamente (usando lógica, não apenas
# atribuindo diretamente) um vetor numérico com 10 posições, conforme abaixo:
# 5 3 5 3 5 3 5 3 5 3
# 0 1 2 3 4 5 6 7 8 9
tamanho = 10

vetor1 = []

for i in range(tamanho):
    if i % 2 == 0:
        vetor1.append(5)
    else:
        vetor1.append(3)

for i in range(tamanho):
    print(vetor1[i], end=" ")
print()
for i in range(tamanho):
    print(i, end=" ")

