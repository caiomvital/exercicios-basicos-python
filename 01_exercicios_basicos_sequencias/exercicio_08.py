# 8) Desenvolva um programa que leia uma distância em metros e mostre os valores
# relativos em outras medidas.
# Ex:
# Digite uma distância em metros: 185.72
# A distância de 85.7m corresponde a:
# 0.18572Km # 1.8572Hm
# 18.572Dam # 1857.2dm
# 18572.0cm # 185720.0mm

distancia_em_m = float(input("Digite uma distância em metros: "))
distancia_em_km = distancia_em_m / 1000
distancia_em_hm = distancia_em_m / 100
distancia_em_dam = distancia_em_m / 10
distancia_em_dm = distancia_em_m * 10
distancia_em_cm = distancia_em_m * 100
distancia_em_mm = distancia_em_m * 1000

print(f"A distância de {distancia_em_m}m corresponde a: ")
print(f"{distancia_em_km}km | {distancia_em_hm}hm | {distancia_em_dam}dam")
print(f"{distancia_em_dm}dm | {distancia_em_cm}cm | {distancia_em_mm}mm")
