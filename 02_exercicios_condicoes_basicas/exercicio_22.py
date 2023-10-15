# 22) Escreva um programa que leia o ano de nascimento de um rapaz e mostre a sua
# situação em relação ao alistamento militar.
#  - Se estiver antes dos 18 anos, mostre em quantos anos faltam para o
# alistamento.
#  - Se já tiver depois dos 18 anos, mostre quantos anos já se passaram do
# alistamento.

ano_nascimento = int(input("Digite o ano do nascimento: "))
ano_atual = 2023
idade = ano_atual - ano_nascimento

if idade > 18:
    tempo_passado = idade - 18
    print(f"Já se passaram {tempo_passado} anos desde o alistamento")
elif idade < 18:
    tempo_passado = 18 - idade
    print(f"Faltam {tempo_passado} anos para o alistamento.")