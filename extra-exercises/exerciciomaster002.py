from time import sleep

sleep(0.6)
print("-=-" * 11)
sleep(0.6)
print("Seja bem vindo a Loja do Bairro!")
sleep(0.6)
print("-=-" * 11)
sleep(1)

nome_produto = str(input("Nome do produto: "))
preco_produto = float(input("Preço do produto: "))
quantidade_comprada = int(input("Quantidade comprada do produto: "))
valor_entregou = float(input("Valor que entregou para pagar: "))

total_compra = preco_produto * quantidade_comprada

print(f"Produto: {nome_produto}")
print(f"Preço do produto: R$ {preco_produto:.2f}")
print(f"Quantidade comprada: {quantidade_comprada}")
print(f"Valor pago: R$ {valor_entregou:.2f}")
print(f"Total da compra: R$ {total_compra:.2f}")

if valor_entregou == total_compra:
    print("Pagamento exato.")
else:
    if valor_entregou > total_compra:
        troco = valor_entregou - total_compra
        print(f"Troco: R$ {troco:.2f}")
    else:
        faltou = total_compra - valor_entregou
        print(f"Faltou: R$ {faltou:.2f}")
