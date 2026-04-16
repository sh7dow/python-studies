preco_de_custo = float(input("Qual foi o preço de custo? R$"))
preco_de_venda = float(input("Qual foi o preço que foi vendido? R$"))

prejuizo_ou_lucro = (preco_de_venda - preco_de_custo) / preco_de_custo * 100

print(f"Preço de custo: {preco_de_custo:.2f}")
print(f"Preço de venda: {preco_de_venda:.2f}")
print(f"Lucro ou Prejuizo: {prejuizo_ou_lucro:.2f}%")