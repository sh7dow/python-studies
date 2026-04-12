"""
Passo a passo:
1. Eleva cateto oposto ao quadrado
2. Eleva cateto adjacente ao quadrado
3. Soma os dois
4. Tira a raiz quadrada
5. Mostra o resultado

Exemplo com 3 e 4:
3 ** 2 = 9
4 ** 2 = 16
9 + 16 = 25
√25 = 5
Hipotenusa = 5

Passo a passo da hipotenusa ^^^^^^^^^^^^^^^^^^^^^^^^
"""

from math import hypot

comprimento_co = float(input("Qual o comprimento do cateto oposto? "))
comprimento_ca = float(input("Qual o comprimento do cateto adjacente? "))

hi = hypot(comprimento_co, comprimento_ca)

print(f"A hipotenusa vai medir {hi:.2f}")