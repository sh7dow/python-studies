# Usei IA pra fazer os comentários

# Pede o primeiro número
a = int(input("Digite um número: "))

# Pede o segundo número
b = int(input("Digite outro número: "))

# Pede o terceiro número
c = int(input("Digite mais um número: "))

# Começa supondo que o menor número e o primeiro
menor = a

# Se b for menor que a e menor que c, então b é o menor
if b < a and b < c:
    menor = b

# Se c for menor que b e menor que a, então c é o menor
if c < b and c < a:
    menor = c

# Começa supondo que o maior número e o primeiro
maior = a

# Se b for maior que a e maior que c, então b é o maior
if b > a and b > c:
    maior = b

# Se c for maior que a e maior que b, então c é o maior
if c > a and c > b:
    maior = c

# Mostra qual foi o menor número
print(f"O menor número é o: {menor}")

# Mostra qual foi o maior número
print(f"O maior número é o: {maior}")
