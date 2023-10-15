# 55) [DESAFIO] Vamos melhorar o jogo que fizemos no exercício 32. A partir de
# agora, o computador vai sortear um número entre 1 e 10 e o jogador vai ter 4
# tentativas para tentar acertar.

import random

numero_aleatorio = random.randint(1, 10)
tentativas = 0
numero_tentado = 0

while tentativas < 4:
    numero_tentado = int(input("Digite um número:"))
    if numero_tentado == numero_aleatorio:
        print("Acertou!")
        break
    else:
        print("Errou!")
        tentativas += 1
print(f"O número sorteado foi {numero_aleatorio}")
