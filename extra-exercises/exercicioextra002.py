"""
Pedi ao Claude IA alguns desafios com os temas que estou estudando, ele fez esse:

Desafio 1: DESCONTO (Fácil)
O que fazer:

Pedir o preço de um produto
Pedir o percentual de desconto
Calcular e mostrar o preço final
"""

preco_produto = float(input("Qual o preço do produto? R$"))
quantidade_desconto = float(input("Quanto de desconto você quer? "))

valor_desconto = preco_produto * quantidade_desconto / 100
preco_final = preco_produto - valor_desconto

print(f"O produto que era R${preco_produto:.2f} agora é R${preco_final:.2f} com o desconto de {quantidade_desconto:.2f}%!")