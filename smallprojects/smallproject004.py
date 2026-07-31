# Crie um programa chamado Cadastro para Viagem.
from time import sleep

sleep(0.6)
print("-=-" * 14)
sleep(0.6)
print("Seja bem vindo ao Cadastro para Viagem.")
sleep(0.6)
print("=-=" * 14)
sleep(0.6)

nome_pessoa = str(input("Qual o seu nome? "))
idade = int(input("Qual sua idade? "))
preco_passagem = float(input("Qual o preço da passagem? "))

if idade <= 12:
    passagem = "Passagem infantil"
    cinquenta_porcento_passagem = preco_passagem - preco_passagem * 50 / 100
    valor_final = f"R$: {cinquenta_porcento_passagem:.2f}"
else:
    if idade < 60:
        passagem = "Passagem normal"
        valor_final = f"R$: {preco_passagem:.2f}"
    else:
         passagem = "Passagem sênior"
         setenta_porcento_passagem = preco_passagem - preco_passagem * 70 / 100
         valor_final = f"R$: {setenta_porcento_passagem:.2f}"

print(f"Nome: {nome_pessoa}")
print(f"Idade: {idade}")
print(f"Tipo: {passagem}")
print(f"Valor final: {valor_final}")
