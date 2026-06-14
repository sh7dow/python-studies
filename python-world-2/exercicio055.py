peso_maior = 0
peso_menor = 0

for p in range(1, 6):
    peso = float(input(f"Peso da {p} pessoa (Kg): "))

    if p == 1:
        peso_maior = peso
        peso_menor = peso
    else:
        if peso > peso_maior:
            peso_maior = peso
        if peso < peso_menor:
            peso_menor = peso

print(f"O peso maior é: {peso_maior}Kg")
print(f"O peso menor é: {peso_menor}Kg")
