"""
Desafio 2: COMISSÃO (Fácil-Médio)
O que fazer:

Um vendedor recebe uma comissão de 5% sobre as vendas
Pedir o valor total de vendas
Calcular quanto de comissão ele ganha
Mostrar o valor da comissão
"""

valor_das_vendas = float(input("Valor de vendas: R$"))
comissao = valor_das_vendas * 5 / 100

print(f"O vendedor vendeu R${valor_das_vendas:.2f}, entao ele teve R${comissao:.2f} de comissão! (5%)")