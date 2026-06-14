primeiro_termo = int(input("Qual é o primeiro termo? "))
razao = int(input("Qual é a razão? "))

contador = 0
termo = primeiro_termo

while contador < 10:
    print(termo, end=" -> ")
    termo = termo + razao
    contador = contador + 1

print("FIM")