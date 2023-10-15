# 5) Faça um programa que leia as duas notas de um aluno em uma matéria e mostre
# na tela a sua média na disciplina.
# Ex:
# Nota 1: 4.5
# Nota 2: 8.5
# A média entre 4.5 e 8.5 é igual a 6.5

primeira_nota = float(input("Entre com a primeira nota: "))
segunda_nota = float(input("Entre om a segunda nota: "))
media = (primeira_nota + segunda_nota) / 2
print(f"A média entre {primeira_nota} e {segunda_nota} é igual a {media}.")