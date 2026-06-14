numero = int(input("Digite um número: "))

fatorial = 1
contador = numero

while contador > 0:
    fatorial = fatorial * contador
    contador = contador - 1

print(f"O fatorial de {numero} é {fatorial}")