aresp = 'S'
media = 0
soma = 0
quantidade = 0
maior = 0
menor = 0

while resp in 'Ss':
    num = int(input("Digite um número: "))
    soma = soma + num
    quantidade = quantidade + 1

    if quantidade == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    resp = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
media = soma / quantidade
print(f"Você digitou {quantidade} números e a média foi {media}")
print(f"O maior valor foi {maior} e o menor foi {menor}")