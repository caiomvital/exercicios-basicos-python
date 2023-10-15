# 97) Refaça o exercício 91, só que agora em forma de função Maior(), mas faça uma
# adaptação que vai receber TRÊS números como parâmetro e vai retornar qual foi o
# maior entre eles.

def Maior(a, b, c):
    return max(a, b, c)


# --- chamando a função
a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o terceiro valor: "))

print(Maior(a, b, c))
