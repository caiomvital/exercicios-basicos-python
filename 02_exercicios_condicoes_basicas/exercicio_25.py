# 25) [DESAFIO] Crie um programa que leia o tamanho de três segmentos de reta.
# Analise seus comprimentos e diga se é possível formar um triângulo com essas
# retas. Matematicamente, para três segmentos formarem um triângulo, o comprimento
# de cada lado deve ser menor que a soma dos outros dois.

primeiro_segmento = int(input("Digite o valor do primeiro segmento de reta: "))
segundo_segmento = int(input("Digite o valor do segundo segmento de reta: "))
terceiro_segmento = int(input("Digite o valor do terceiro segmento de reta: "))

if (primeiro_segmento + segundo_segmento) > terceiro_segmento \
        or (segundo_segmento + terceiro_segmento) > primeiro_segmento \
        or (terceiro_segmento + primeiro_segmento) > segundo_segmento:
    print("É possível formar um triângulo com os três segmentos fornecidos.")
else:
    print("Não é possível formar um triângulo com os três segmentos fornecidos.")