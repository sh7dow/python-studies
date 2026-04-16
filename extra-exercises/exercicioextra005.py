"""
Desafio 4: COMPARAÇÃO DE DESCONTOS (Médio)

O que fazer:
- Pedir o preço de um produto
- Mostrar 3 opções:
   - Desconto de 10%
   - Desconto de 15%
   - Desconto de 20%
- Mostrar quanto o cliente economiza em cada caso:
"""

preco_do_produto = float(input("Qual é o preço do produto? R$"))

desconto_10_porcento = preco_do_produto - (preco_do_produto * 10 / 100)
desconto_15_porcento = preco_do_produto - (preco_do_produto * 15 / 100)
desconto_20_porcento = preco_do_produto - (preco_do_produto * 20 / 100)

economia_10_porcento = preco_do_produto - desconto_10_porcento
economia_15_porcento = preco_do_produto - desconto_15_porcento
economia_20_porcento = preco_do_produto - desconto_20_porcento


print(f"O seu produto com desconto de 10% é: R${desconto_10_porcento:.2f}, e você economizou R${economia_10_porcento:.2f}")
print(f"O seu produto com desconto de 15% é: R${desconto_15_porcento:.2f}, e você economizou R${economia_15_porcento:.2f}")
print(f"O seu produto com desconto de 20% é: R${desconto_20_porcento:.2f}, e você economizou R${economia_20_porcento:.2f}")