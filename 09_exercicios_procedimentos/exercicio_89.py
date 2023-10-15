# 89) Crie um programa que melhore o procedimento Gerador() da questão anterior
# para que o programador possa escolher uma entre três bordas:
#  +-------=======------+ Borda 1
#  ~~~~~~~~:::::::~~~~~~~ Borda 2
#  <<<<<<<<------->>>>>>> Borda 3
# Ex: Uma chamada válida seria Gerador("Portugol Studio", 3, 2)
# ~~~~~~~~:::::::~~~~~~~
#  Portugol Studio
#  Portugol Studio
#  Portugol Studio
# ~~~~~~~~:::::::~~~~~~~

def Gerador(borda, mensagem, quantidade):
    print("Escolha a borda:")
    opcao = int(input("1 para +-------=======------+\n2 para ~~~~~~~~:::::::~~~~~~~\n3 para <<<<<<<<------->>>>>>>\n"))
    if opcao == 1:
        borda = "+-------=======------+"
    elif opcao == 2:
        borda = "~~~~~~~~:::::::~~~~~~~"
    elif opcao == 3:
        borda = "<<<<<<<<------->>>>>>>"
    print(borda)
    for i in range(quantidade):
        print(mensagem)
    print(borda)

# --- chamando a função

mensagem = input("Digite a mensagem que deseja que apareça:")
quantidade = int(input("Digite a quantidade de vezes que deseja que a mensagem apareça:"))
Gerador(0, mensagem, quantidade)




