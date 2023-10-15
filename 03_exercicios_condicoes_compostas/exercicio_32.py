# 32) [DESAFIO] Crie um jogo onde o computador vai sortear um número entre 1 e 5 o
# jogador vai tentar descobrir qual foi o valor sorteado.
import random

numero_sorteado = random.randint(1, 5)
numero_tentado = int(input("Tente adivinhar um número de 1 a 5: "))

if numero_tentado == numero_sorteado:
    print(f"Parabéns, você acertou! O número sorteado foi {numero_sorteado}!")
else:
    print(f"Sinto muito, você errou! O número sorteado foi {numero_sorteado}!")
