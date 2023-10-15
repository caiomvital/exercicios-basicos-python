# 82) Faça um algoritmo que leia a nota de 10 alunos de uma turma e guarde-as em
# um vetor. No final, mostre:
# a) Qual é a média da turma
# b) Quantos alunos estão acima da média da turma
# c) Qual foi a maior nota digitada
# d) Em que posições a maior nota aparece

tamanho = 10
vetor = []
media = 0
soma_notas = 0
quantidade_acima_da_media = 0
maior_nota = None
for i in range(tamanho):
    vetor.append(float(input(f"Digite a nota do aluno #{i + 1}: ")))
    soma_notas += vetor[i]
    if maior_nota is None or maior_nota < vetor[i]:
        maior_nota = vetor[i]
media = soma_notas / len(vetor)
for i in range(len(vetor)):

    if vetor[i] > media:
        quantidade_acima_da_media += 1

# a) Qual é a média da turma
print(f"A média da turma é{media: .2f}")
# b) Quantos alunos estão acima da média da turma
print(f"A turma tem {quantidade_acima_da_media} alunos acima da média.")
# c) Qual foi a maior nota digitada
print(f"A maior nota digitada foi{maior_nota: .2f}")
# d) Em que posições a maior nota aparece
for i in range(len(vetor)):
    if vetor[i] == maior_nota:
        print(f"A maior nota aparece na posição #{i}.")