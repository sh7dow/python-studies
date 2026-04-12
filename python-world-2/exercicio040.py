nota1 = float(input("Qual a primeira nota do aluno? "))
nota2 = float(input("Qual a segunda nota do aluno? "))

media = (nota1 + nota2) / 2

if media < 5:
    print("Reprovado.")
elif media == 5 or media <= 7:
    print("Recuperação.")
elif media > 7:
    print("Aprovado.")