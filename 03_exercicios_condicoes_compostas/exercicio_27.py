# 27) Crie um programa que leia duas notas de um aluno e calcule a sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
#  - Média até 4.9: REPROVADO
#  - Média entre 5.0 e 6.9: RECUPERAÇÃO
#  - Média 7.0 ou superior: APROVADO

primeira_nota = float(input("Digite a primeira nota: "))
segunda_nota = float(input("Digite a segunda nota: "))
media = (primeira_nota + segunda_nota) / 2

if media <= 4.9:
    print("Reprovado!")
elif 4.9 < media <= 6.9:
    print("Recuperação!")
elif media >= 7:
    print("Aprovado!")
