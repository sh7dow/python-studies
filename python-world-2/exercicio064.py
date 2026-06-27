somanumeros = 0
contador = 0

numeros = int(input("Digite os números: "))

while numeros != 999:
    somanumeros = somanumeros + numeros
    contador = contador + 1

    numeros = int(input("Digite os números: "))

print("Você digitou a flag. Programa ENCERRADO.")
print(f"A soma dos números foi: {somanumeros}, e a quantidade de números foi: {contador}.")