from math import radians, sin, cos, tan

graus = float(input("Qual o ângulo? "))

radianos = radians(graus)
seno = sin(radianos)
cosseno = cos(radianos)
tangente = tan(radianos)


print(f"Entrada: {graus}")
print(f"Cálculo: Seno {seno:.2f}")
print(f"Cálculo: Cosseno {cosseno:.2f}")
print(f"Cálculo: Tangente {tangente:.2f}")
