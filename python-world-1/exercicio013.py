# Aumento do salário do funcionário

salario = float(input("Qual o seu salário? R$"))
aumento_15 = salario * 15 / 100
salario_final = salario + aumento_15

print(f"O salário que era R${salario:.2f}, agora é R${salario_final:.2f} devido ao aumento de 15%!")