import math

cateto_oposto = float(input("Qual é o cateto oposto? "))
cateto_adjacente = float(input("Qual é o cateto adjacente? "))

hipotenusa = math.sqrt(cateto_oposto ** 2 + cateto_adjacente ** 2)

print(f"Cateto 1: {cateto_oposto:.2f}")
print(f"Cateto 2: {cateto_adjacente:.2f}")
print(f"Hipotenusa: {hipotenusa:.2f}")
