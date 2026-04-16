soma = 0 # Armazena o valor

for n in range(1, 7):
    numero = int(input("Digite um número: "))

    if numero % 2 == 0: # Vê se o número é par
        soma = soma + numero # Se for par vai executar esse código
    if numero % 2 == 1: # Vê se o número é impar
        soma = soma + 0 # Se for impar então só vai somar com 0 ou seja vai ignorar

print(soma)