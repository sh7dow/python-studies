numero_usuario = int(input("Digite um número: "))
soma = 0

if numero_usuario == 0:
        print("Você digitou 0 de primeira! Portanto, não teve nenhuma soma.")

while numero_usuario != 0:

    soma = soma + numero_usuario
    
    numero_usuario = int(input("Digite um número: "))

    if numero_usuario == 0:
        print(f"Você digitou 0! A soma de todos os números foi: {soma}")