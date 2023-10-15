# 69) [DESAFIO] Desenvolva um programa que leia o primeiro termo e a razão de uma
# PA (Progressão Aritmética), mostrando na tela os 10 primeiros elementos da PA e
# a soma entre todos os valores da sequência.

primeiro_termo = int(input("Digite o primeiro termo da progressão aritmética: "))
razao = int(input("Digite a razão da progressão aritmética: "))
soma = 0

print("Os 10 primeiros elementos da progressão aritmética são: ")

for i in range(10):
    termo = primeiro_termo + i * razao
    print(termo, end=" ")
    soma += termo

print(f"A soma dos elementos da progressão aritmética é: {soma}.")
