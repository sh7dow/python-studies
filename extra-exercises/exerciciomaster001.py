# Desafio
# Crie um programa chamado Central do Aluno

nome_aluno = str(input("Qual o nome do aluno? "))
ano_de_nascimento = int(input("Qual o ano que o aluno nasceu? "))
nota_1 = float(input("Qual a primeira nota do aluno? "))
nota_2 = float(input("Qual é a segunda nota do aluno? "))
valor_mensalidade = float(input("Qual o valor da mensalidade do aluno? "))

idade = 2026 - ano_de_nascimento
media = (nota_1 + nota_2) / 2

if media >= 7:
    situacao = "Aprovado"
    mensalidade_10_porcento = valor_mensalidade - valor_mensalidade * 10 / 100
    mensalidade_final = mensalidade_10_porcento
else:
    if media >= 5:
        situacao = "Recuperação"
        mensalidade_normal = valor_mensalidade
        mensalidade_final = mensalidade_normal
    else:
        situacao = "Reprovado"
        mensalidade_normal = valor_mensalidade
        mensalidade_final = mensalidade_normal

print(f"Aluno: {nome_aluno}")
print(f"Idade: {idade}")
print(f"Média: {media:.2f}")
print(f"Situação: {situacao}")
print(f"Mensalidade: R$ {mensalidade_final}")