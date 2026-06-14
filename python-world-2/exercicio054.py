import datetime

ano = datetime.date.today().year
maiores = 0
menores = 0

for c in range(1, 8):
    ano_nascimento = int(input(f"Em que ano a {c} pessoa nasceu? "))
    verificacao = ano - ano_nascimento

    if verificacao >= 21:
        maiores = maiores + 1
    else:
        menores = menores + 1

print(f"Tem {maiores} pessoas maior(es) de idade.")
print(f"E também tivemos {menores} pessoas menor(es) de idade.")
