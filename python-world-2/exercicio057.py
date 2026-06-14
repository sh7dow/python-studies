sexo = str(input("Digite o seu sexo: (M/F) ")).upper()

while sexo != 'M' and sexo != 'F':
    sexo = str(input("Inválido! Digite M (Masculino) ou F (Feminino): ").upper())
if sexo == 'M' or sexo == 'F':
    print("O valor digitado está correto.")

print(f"Sexo: {sexo}")