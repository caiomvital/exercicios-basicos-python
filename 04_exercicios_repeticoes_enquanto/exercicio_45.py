# 45) O programa anterior vai ter um problema quando digitarmos o primeiro valor
# maior que o último. Resolva esse problema com um código que funcione em qualquer
# situação.

primeiro_valor = int(input("Digite o primeiro valor:"))
ultimo_valor = int(input("Digite o último valor:"))
incremento = int(input("Digite o incremento:"))

if primeiro_valor > ultimo_valor:
    print("O último valor é menor que o primeiro. A contagem será feita de forma regressiva:")
    while ultimo_valor < primeiro_valor:
        print(primeiro_valor, end=" ")
        primeiro_valor -= incremento
else:
    while primeiro_valor < ultimo_valor:
        print(primeiro_valor, end=" ")
        primeiro_valor += incremento
print("Acabou!")

