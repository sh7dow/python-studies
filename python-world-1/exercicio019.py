from random import choice

nome1 = str(input("Qual o nome do primeiro aluno? "))
nome2 = str(input("Qual o nome do segundo aluno? "))
nome3 = str(input("Qual o nome do terceiro aluno? "))
nome4 = str(input("Qual o nome do quarto aluno? "))

lista = [nome1, nome2, nome3, nome4]

escolhido = choice(lista)

print(f"O aluno escolhido foi {escolhido}!")