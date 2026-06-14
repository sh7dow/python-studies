primeiro_termo = int(input("Qual é o primeiro termo? "))
razao = int(input("Qual é a razão? "))

contador = 0
termo = primeiro_termo
mais = 10

while mais != 0:
    contador = 0

    while contador < mais:
        print(termo, end= ' -> ')
        termo = termo + razao
        contador = contador + 1

    mais = int(input("Quer mostrar mais quantos termos? "))
print("FIM")