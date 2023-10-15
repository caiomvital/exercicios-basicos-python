# 100) Melhore o exercício 96, criando além da função Media() uma outra função
# chamada Situacao(), que vai retornar para o programa principal se o aluno está
# APROVADO, em RECUPERAÇÃO ou REPROVADO. Essa nova função, vai receber como
# parâmetro o resultado retornado pela função Media().

def Media(a, b):
    media = (a + b) / 2
    return media


def Situacao(media):
    if media >= 7.0:
        return "Aprovado"
    elif 4.5 <= media <= 6.9:
        return "Recuperação"
    elif media < 4.5:
        return "Reprovado"


# --- chamando as funções

print(Situacao(Media(7, 1)))
