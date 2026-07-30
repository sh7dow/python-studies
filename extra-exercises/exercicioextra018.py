contador = 0

for pessoas in range(1, 6):
    idadepessoas = int(input("Qual sua idade? "))

    if idadepessoas >= 18:
        contador = contador + 1

if contador == 1:
    print(f"{contador} pessoa é maior de idade.")
else:
    print(f"{contador} pessoas são maiores de idade.")