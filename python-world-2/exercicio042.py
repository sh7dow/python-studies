r1 = float(input("Diga o valor da primeira reta: "))
r2 = float(input("Diga o valor da segunda reta: "))
r3 = float(input("Diga o valor da terceira reta: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r3:
    print("Pode formar triângulo.")
else:
    print("Não forma um triângulo.")

if r1 == r2 == r3:
    print("É um triângulo equilátero")
elif r1 == r2 or r1 == r3 or r2 == r3:
    print("É um triângulo isósceles")
else:
    print("É um triângulo escaleno")
