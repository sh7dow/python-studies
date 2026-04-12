# O trunc transforma números em números naturais, ou seja, em inteiros.

from math import trunc

num = float(input("Digita um número: "))
parte_inteira = trunc(num)

print(f"O número {num} tem a parte de inteira de {parte_inteira}")