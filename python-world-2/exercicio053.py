frase = str(input("Diga uma frase qualquer: ")).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto) - 1, -1, -1):
    inverso = inverso + junto[letra]
print(f"O inverso de {junto} é {inverso}.")

if inverso == junto:
    print("Então \033[1;32mÉ PALÍNDROMO!")
else:
    print("Portanto, \033[1;31mNÃO É PALÍNDROMO!")
