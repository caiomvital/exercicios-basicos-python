# 96) Crie um programa que tenha uma função Media(), que vai receber as 2 notas de
# um aluno e retornar a sua média para o programa principal.

def Media(nota1, nota2):
    total = nota1 + nota2
    return total / 2


# --- chamando a função

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

print(f"A média do aluno é{Media(nota1, nota2): .2f}")