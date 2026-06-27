numero = int(input("Digite seu número: "))

t1 = 0
t2 = 1
contador = 0

while contador < numero:
    print(t1, end=' -> ')

    t3 = t1 + t2
    t1 = t2
    t2 = t3

    contador = contador + 1
print("FIM")
