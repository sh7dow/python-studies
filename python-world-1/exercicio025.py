nome_pessoa = input("Qual é o seu nome? ").strip().lower()
contagem_de_silvas = nome_pessoa.lower().count('silva')

print(f"Silva aparece no nome?")
print("silva" in nome_pessoa.lower())
print(f"Silva aparece {contagem_de_silvas} vez(es)!")