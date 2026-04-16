nome_motorista = str(input("Qual o nome do motorista? "))
velocidade_carro = int(input("Qual a velocidade do carro? "))

if velocidade_carro <= 80:
    situacao = "Dentro do limite."
else:
    situacao = "Multado."

print(f"Motorista: {nome_motorista}")
print(f"Velocidade: {velocidade_carro} km/h")
print(f"Situação: {situacao}")

if velocidade_carro > 80:
    acima_do_limite = velocidade_carro - 80
    valor_multa = acima_do_limite * 7
    print(f"Valor da multa: R${valor_multa:.2f}")

if velocidade_carro >= 100:
    print("Sua velocidade está muito alta. Dirija com cuidado.")
