somaimpares = 0

for c in range(0, 500+1):
    if c % 2 == 1 and c % 3 == 0:
        somaimpares += c
        print(somaimpares)