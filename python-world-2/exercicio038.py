primeiro_valor = int(input("Qual o primeiro valor? "))
segundo_valor = int(input("Qual o segundo valor? "))

if primeiro_valor > segundo_valor:
    print("O primeiro valor é maior")
elif segundo_valor > primeiro_valor:
    print("O segundo valor é maior")
else:
    print("Não existe maior ou menor, os dois valores são iguais.")