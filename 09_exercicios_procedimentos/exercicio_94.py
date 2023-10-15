# 94) [DESAFIO] Desenvolva um aplicativo que tenha um procedimento chamado
# Fibonacci() que recebe um único valor inteiro como parâmetro, indicando quantos
# termos da sequência serão mostrados na tela. O seu procedimento deve receber
# esse valor e mostrar a quantidade de elementos solicitados.
# Obs: Use os exercícios 70 e 75 para te ajudar na solução
# Ex:
# Fibonacci(5) vai gerar 1 >> 1 >> 2 >> 3 >> 5 >> FIM
# Fibonacci(9) vai gerar 1 >> 1 >> 2 >> 3 >> 5 >> 8 >> 13 >> 21 >> 34 >> FIM

def Fibonacci(valor):
    termo1 = 1
    termo2 = 1
    contador = 0

    while contador < valor:
        print(termo1, end=" >> ")
        proximo_termo = termo1 + termo2
        termo1, termo2 = termo2, proximo_termo
        contador += 1

    print("FIM")


# ------- chamando a função

Fibonacci(5)