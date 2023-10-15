# 19) Crie um algoritmo que leia o nome e as duas notas de um aluno, calcule a sua
# média e mostre na tela. No final, analise a média e mostre se o aluno teve ou
# não um bom aproveitamento (se ficou acima da média 7.0).

primeira_nota = float(input("Digite a primeira nota: "))
segunda_nota = float(input("Digite a segunda nota: "))
media = (primeira_nota + segunda_nota) / 2

if media >= 7:
    print(f"Aluno teve bom aproveitamento! Média {media}.")
else:
    print(f"Aluno não teve bom aproveitamento! Média {media}")