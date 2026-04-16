"""
Desafio 3: IMPOSTO (Médio)
O que fazer:

Um produto custa X reais
Tem um imposto de 8% sobre o preço
Mostrar o preço original, o imposto, e o preço final (com imposto)
"""

preco_do_produto = float(input("Qual o preço do produto? R$"))
imposto = preco_do_produto * 8 / 100
preco_final = preco_do_produto + imposto

print(f"Produto: R${preco_do_produto:.2f}")
print(f"Imposto (8%): R${imposto:.2f}")
print(f"Preço final: R${preco_do_produto:.2f} + R${imposto:.2f} = R${preco_final:.2f}")