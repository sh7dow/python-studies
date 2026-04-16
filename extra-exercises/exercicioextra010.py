import math

x1 = float(input("X: "))
y1 = float(input("Y: "))
x2 = float(input("X: "))
y2 = float(input("Y: "))

distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print(f"Ponto 1 - X: {x1:.2f}, Y: {y1:.2f}")
print(f"Ponto 2 - X: {x2:.2f}, Y: {y2:.2f}")
print(f"Distância: {distancia:.2f}")
