pergunta_nome = input("Qual seu nome? ")
dividindoprimeiro = pergunta_nome.split()[0].upper()
dividindoultimo = pergunta_nome.split()[-1].upper()

print(f"Primeiro: {dividindoprimeiro}")
print(f"Último: {dividindoultimo}")