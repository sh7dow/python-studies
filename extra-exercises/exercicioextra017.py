numero = int(input("Digite um número: "))
soma = 0

while numero != 0:
    soma = soma + numero
    numero = int(input("Digite um número: "))

print(f"Você digitou 0. A soma dos números foi {soma}")