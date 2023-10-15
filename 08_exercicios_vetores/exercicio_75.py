# 75) Crie um programa que preencha automaticamente (usando lógica, não apenas
# atribuindo diretamente) um vetor numérico com 15 posições com os primeiros
# elementos da sequência de Fibonacci:
# 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14

tamanho = 15

vetor = []

termo1 = 1
termo2 = 1

for i in range(tamanho):
    vetor.append(termo1)
    termo1, termo2 = termo2, termo1 + termo2

for i in range(tamanho):
    print(vetor[i], end=" ")
print()
for i in range(tamanho):
    print(i, end=" ")

