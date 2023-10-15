# 70) [DESAFIO] Faça um programa que mostre os 10 primeiros elementos da Sequência
# de Fibonacci:
# 1 1 2 3 5 8 13 21...

primeiro_termo = 1
segundo_termo = 1
proximo_termo = 0

print(primeiro_termo)
print(segundo_termo)

for i in range(8):
    proximo_termo = primeiro_termo + segundo_termo
    print(proximo_termo)

    aux = primeiro_termo
    primeiro_termo = segundo_termo
    segundo_termo = proximo_termo
