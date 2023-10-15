# 28) Faça um programa que leia a largura e o comprimento de um terreno
# retangular, calculando e mostrando a sua área em m². O programa também
# devemostrar a classificação desse terreno, de acordo com a lista abaixo:
#  - Abaixo de 100m² = TERRENO POPULAR
#  - Entre 100m² e 500m² = TERRENO MASTER
#  - Acima de 500m² = TERRENO VIP

largura_terreno = int(input("Digite a largura do terreno em m²: "))
comprimento_terreno = int(input("Digite o comprimento do terreno em m²: "))
area = largura_terreno * comprimento_terreno

if area < 100:
    print(f"Terreno de {area}m². TERRENO POPULAR.")
elif 100 <= area < 500:
    print(f"Terreno de {area}m². TERRENO MASTER.")
elif area >= 500:
    print(f"Terreno de {area}m². TERRENO VIP.")
