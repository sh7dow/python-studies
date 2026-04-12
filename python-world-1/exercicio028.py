from random import randint
from time import sleep

print("-=-" * 18)
print("Vou pensar em um número de 0 a 5, tente adivinhar.")
print("-=-" * 18)

numero_aleatorio = randint(0, 5) # Faz o computador "pensar" em um número aleatório
numero_usuario = int(input("Qual número eu pensei? ")) # Jogador tenta adivinhar

print("PROCESSANDO...")
sleep(3)

if numero_usuario == numero_aleatorio:
    print("PARABÉNS! Você me venceu.")
else:
    print(f"VOCÊ PERDEU!, eu pensei no número {numero_aleatorio} e não no número {numero_usuario}!")
