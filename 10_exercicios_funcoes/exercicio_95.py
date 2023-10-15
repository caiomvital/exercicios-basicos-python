# 95) Refaça o exercício 90, só que agora em forma de função Somador(), que vai
# receber dois parâmetros e vai retornar o resultado da soma entre eles para o
# programa principal.

def Somador(a, b):
    return a + b


# ----- chamando a função
a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))

print(f"O valor da soma é {Somador(a, b)}.")