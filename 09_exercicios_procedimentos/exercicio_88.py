# 88) Crie um programa que melhore o procedimento Gerador() da questão anterior
# para que mostre uma mensagem vário
# Ex: Ao chamar Gerador("Aprendendo Portugol", 4) aparece:
# +-------=======------+
#  Aprendendo Portugol
#  Aprendendo Portugol
#  Aprendendo Portugol
#  Aprendendo Portugol
# +-------=======------+

def Gerador(mensagem, quantidade):
    print("+-------=======------+")
    for i in range(quantidade):
        print(mensagem)
    print("+-------=======------+")

# ----- chamando a função
mensagem = "Aprendendo Python"
quantidade = int(input("Digite a quantidade de vezes que deseja que apareça a mensagem:"))

Gerador(mensagem, quantidade)
