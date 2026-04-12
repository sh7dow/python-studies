from datetime import datetime

ano_nascimento = int(input("Qual o ano de nascimento? "))

idade = datetime.today().year - ano_nascimento

if idade <= 9:
    print("MIRIM")
elif idade <= 14:
    print("INFANTIL")
elif idade <= 19:
    print("JUNIOR")
elif idade <= 20:
    print("SÊNIOR")
else:
    print("MASTER")