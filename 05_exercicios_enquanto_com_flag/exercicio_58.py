# 58) Faça um algoritmo que leia a idade de vários alunos de uma turma. O programa
# vai parar quando for digitada a idade 999. No final, mostre quantos alunos
# existem na turma e qual é a média de idade do grupo.

idade = 0
quantidade_alunos = 0
soma_idades = 0
media_idades = 0

while idade != 999:
    idade = int(input("Digite a idade de um aluno ou digite 999 para encerrar: "))

    if idade != 999:
        soma_idades += idade
        quantidade_alunos += 1
media = soma_idades / quantidade_alunos
print(f"A quantidade de alunos inseridos foi {quantidade_alunos}.")
print(f"A média de idade dos alunos inseridos é {media}.")

