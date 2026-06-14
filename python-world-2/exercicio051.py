primeiro_termo = int(input("Qual o primeiro termo? "))
razao = int(input("Qual é a razão? "))

termo = primeiro_termo

for c in range(1, 11):
    print(termo, end=' → ')
    termo = termo + razao

print("Fim!")