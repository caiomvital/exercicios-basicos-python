# 18) Faça um programa que leia o ano de nascimento de uma pessoa, calcule a idade
# dela e depois mostre se ela pode ou não votar.

ano_nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = 2023
idade = ano_atual - ano_nascimento

if idade >= 18 and idade < 70 :
    print(f"Com {idade} anos, deve votar.")
elif idade >= 16 and idade < 18 :
    print(f"Com {idade} anos, pode votar.")
else:
    print(f"Com {idade} anos, não pode votar.")

