nome = input("Qual seu nome completo? ").strip()

primeironome = nome.split()[0]
ultimonome = nome.split()[-1]

print(f"O primeiro nome é: {primeironome}")
print(f"O último nome é: {ultimonome}")