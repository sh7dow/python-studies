salario_funcionario = float(input("Qual o salário do funcionário? R$"))

aumento_dez_porcento = salario_funcionario + salario_funcionario * 10 / 100
aumento_quinze_porcento = salario_funcionario + salario_funcionario * 15 / 100

if salario_funcionario >= 1250:
    print(f"O salário do funcionário agora é: R${aumento_dez_porcento:.2f} devido ele ganhar mais de R$1250")
else:
    print(f"O salário do funcionário agora é: {aumento_quinze_porcento:.2f} devido ele ganhar menos ou R$1250")
