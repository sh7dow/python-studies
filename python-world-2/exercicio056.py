somaidade = 0
mediaidade = 0
maioridadehomem = 0
maioridademulher = 0
nomemaisvelho = ''
nomemaisvelha = ''
totmulher20anos = 0

for p in range(1, 5):
    print(f"--------- {p} PESSOA ---------")

    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F] ")).strip()
    somaidade = somaidade + idade

    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomemaisvelho = nome
    if sexo in 'Mm' and idade > maioridadehomem :
        maioridadehomem = idade
        nomemaisvelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20anos = totmulher20anos + 1
        nomemaisvelha = nome
    if sexo in 'Ff' and idade > maioridademulher:
        nomemaisvelha = nome

mediaidade = somaidade / 4

print(f"A média de idade do grupo é de {mediaidade} anos.")
print(f"O homem mais velho tem {maioridadehomem} e se chama {nomemaisvelho}.")
print(f"Ao todo são {totmulher20anos} com menos de 20 anos.")
print(f"E essa mulher é {nomemaisvelha}")
