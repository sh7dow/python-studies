preco_normal_produto = float(input("Diga o preço do produto: "))
print("Opções: \n             Dinheiro     Cartão     2x Cartão     3x ou mais")
condicao_pagamento = str(input("Qual a condição de pagamento? ")).strip().lower()

dez_porcento_desconto = preco_normal_produto - preco_normal_produto * 10 / 100
cinco_porcento_desconto = preco_normal_produto - preco_normal_produto * 5 / 100
vinte_porcento_juros = preco_normal_produto + preco_normal_produto * 20 / 100

if condicao_pagamento == 'dinheiro':
    print(f"Já que você pagou com dinheiro, então agora seu produto é R${dez_porcento_desconto} devido 10% de desconto.")
elif condicao_pagamento == 'cartão':
    print(f"A sua forma de pagamento é o cartão a vista, então agora seu produto custa R${cinco_porcento_desconto} devido 5% de desconto.")
elif condicao_pagamento == '2x cartão':
    print(f"Sua forma de pagamento é 2x no cartão, então não recebe desconto. Seu produto continua R${preco_normal_produto}.")
elif condicao_pagamento == '3x ou mais':
    print(f"A forma de pagamento de 3x ou mais no cartão faz seu produto custar R${vinte_porcento_juros} devido ao juros de 20%.")