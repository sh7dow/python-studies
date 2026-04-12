from datetime import datetime

ano_nascimento = int(input("Qual o seu ano de nascimento? "))

idade = datetime.today().year - ano_nascimento
idade_alistar = 18

if idade < idade_alistar:
    print("Você ainda vai se alistar ao serviço militar.")
    print(f"Faltam {18 - idade} ano(s) para você se alistar.")
elif idade == idade_alistar:
    print("Você já pode se alistar.")
else:
    print("Passou o tempo de se alistar.")
    print(f"{idade - idade_alistar} ano(s) foram excedidos para se alistar.")