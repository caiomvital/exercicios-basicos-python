# 30) [DESAFIO] Refaça o algoritmo 25, acrescentando o recurso de mostrar que tipo
# de triângulo será formado:
#  - EQUILÁTERO: todos os lados iguais
#  - ISÓSCELES: dois lados iguais
#  - ESCALENO: todos os lados diferentes

primeiro_segmento = int(input("Digite o valor do primeiro segmento de reta: "))
segundo_segmento = int(input("Digite o valor do segundo segmento de reta: "))
terceiro_segmento = int(input("Digite o valor do terceiro segmento de reta: "))

if primeiro_segmento == segundo_segmento == terceiro_segmento:
    print("Triângulo Equilátero")
elif (primeiro_segmento == segundo_segmento) or (primeiro_segmento == terceiro_segmento) \
    or (segundo_segmento == terceiro_segmento):
    print("Triângulo Isósceles")
elif primeiro_segmento != segundo_segmento != terceiro_segmento:
    print("Triângulo Escaleno")


