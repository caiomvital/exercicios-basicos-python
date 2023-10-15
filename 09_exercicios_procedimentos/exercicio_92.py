# 92) Crie uma lógica que leia um número inteiro e passe para um procedimento
# ParOuImpar() que vai verificar e mostrar na tela se o valor passado como
# parâmetro é PAR ou ÍMPAR.

def ParOuImpar(valor):
    if valor % 2 == 0:
        print(f"{valor} é par.")
    else:
        print(f"{valor} é ímpar.")


# --- chamando a função

valor = int(input("Digite um valor:"))
ParOuImpar(valor)
