dias = int(input("Por quantos dias o carro foi alugado? "))
km = float(input("Quantos KM foi percorrido com o carro? "))

custo_dias = dias * 60
custo_km = km * 0.15
pago = custo_dias + custo_km

print(f"O total a pagar é de R${pago:.2f}")