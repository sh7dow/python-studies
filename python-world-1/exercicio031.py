distancia_da_viagem = float(input("Qual a distância da viagem? "))


if distancia_da_viagem <= 200:
    preco = distancia_da_viagem * 0.50
else:
    preco = distancia_da_viagem * 0.45

print(f"Você está prestes a começar uma viagem de {distancia_da_viagem} km.")
print(f"A sua passagem será de R${preco:.2f}!")