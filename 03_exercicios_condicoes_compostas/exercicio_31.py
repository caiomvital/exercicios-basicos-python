# 31) [DESAFIO] Crie um jogo de JoKenPo (Pedra-Papel-Tesoura)
import random

opcao = int(input("Entre com 1 para Tesoura, 2 para Papel, 3 para Pedra: "))
opcao_maquina = random.randint(1, 3)

if opcao == 1:
    if opcao_maquina == 1:
        print("Você escolheu tesoura! A máquina escolheu tesoura! Empate!")
    elif opcao_maquina == 2:
        print("Você escolheu tesoura! A máquina escolheu papel! Você ganhou!")
    elif opcao_maquina == 3:
        print("Você escolheu tesoura! A máquina escolheu pedra! A máquina ganhou!")
elif opcao == 2:
    if opcao_maquina == 2:
        print("Você escolheu papel! A máquina escolheu papel! Empate!")
    elif opcao_maquina == 3:
        print("Você escolheu papel! A máquina escolheu pedra! Você ganhou!")
    elif opcao_maquina == 1:
        print("Você escolheu papel! A máquina escolheu tesoura! A máquina ganhou!")
elif opcao == 3:
    if opcao_maquina == 3:
        print("Você escolheu pedra! A máquina escolheu pedra! Empate!")
    elif opcao_maquina == 1:
        print("Você escolheu pedra! A máquina escolheu tesoura! Você ganhou!")
    elif opcao_maquina == 2:
        print("Você escolheu pedra! A máquina escolheu papel! A máquina ganhou!")
else:
    print("Opção Inválida!")