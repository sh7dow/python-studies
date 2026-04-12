valor_casa = float(input("Me informe o valor da casa: R$"))
salario_comprador = float(input("Me informe o salário do comprador da casa: R$"))
anos = int(input("Me informe a quantidade de anos o comprador irá pagar: "))

calculo_meses = anos * 12
prestacao_mensal = valor_casa / calculo_meses
trinta_porcento_salario = salario_comprador * 30 / 100

print(f"Para pagar uma casa de R${valor_casa:.2f} em {anos} anos a prestação será de R${prestacao_mensal:.2f}")

if prestacao_mensal >= trinta_porcento_salario:
    print("Portanto, o empréstimo foi negado.")
else:
    print("Portanto, o empréstimo irá ocorrer normalmente.")