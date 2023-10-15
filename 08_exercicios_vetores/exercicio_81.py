# 81) Crie um programa que leia a idade de 8 pessoas e guarde-as em um vetor. No
# final, mostre:
# a) Qual é a média de idade das pessoas cadastradas
# b) Em quais posições temos pessoas com mais de 25 anos
# c) Qual foi a maior idade digitada (podem haver repetições)
# d) Em que posições digitamos a maior idade

tamanho = 8
vetor = []
media_idades = 0
soma_idades = 0
maior_idade = None
for i in range(tamanho):
    vetor.append(int(input(f"Digite uma idade para a posição #{i}:")))
    soma_idades += vetor[i]

    if maior_idade is None or maior_idade < vetor[i]:
        maior_idade = vetor[i]


# a) Qual é a média de idade das pessoas cadastradas
media_idades = soma_idades / len(vetor)
print(f"A média das idades digitadas é {media_idades}.")
# b) Em quais posições temos pessoas com mais de 25 anos
for i in range(len(vetor)):
    if vetor[i] > 25:
        print(f"Idade acima de 25 encontrada na posição #{i}.")
# c) Qual foi a maior idade digitada (podem haver repetições)
print(f"A maior idade digitada foi {maior_idade}.")
# d) Em que posições digitamos a maior idade
for i in range(len(vetor)):
    if vetor[i] == maior_idade:
        print(f"Maior idade ({maior_idade} anos) encontrada na posição #{i}.")

