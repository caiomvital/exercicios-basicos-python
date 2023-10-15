# 73) Crie um programa que preencha automaticamente (usando lógica, não apenas
# atribuindo diretamente) um vetor numérico com 10 posições, conforme abaixo:
# 9 8 7 6 5 4 3 2 1 0
# 0 1 2 3 4 5 6 7 8 9

tamanho = 10

vetor1 = []
vetor2 = []

for i in range(tamanho):
    valor = 8 + 1 - i
    vetor1.append(valor)
for i in range(tamanho):
    print(vetor1[i], end=" ")
vetor1.sort()
print()
for i in range(tamanho):
    print(vetor1[i], end=" ")
