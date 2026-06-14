import random
from time import sleep

palpites = 1

sleep(.5)
print("-=" * 11)
sleep(.5)
print("Jogo da Adivinhação")
sleep(.5)
print("-=" * 11)
sleep(.5)

numero_jogador = int(input("Escolha um número de 1 a 10: "))
numero_aleatorio = random.randint(1, 10)

while numero_jogador != numero_aleatorio:
    print("Calculando...")
    sleep(.4)
    print("Errou! Tente novamente.")
    sleep(0.4)
    numero_jogador = int(input("Escolha um número de 1 a 10: "))
    palpites = palpites + 1

if numero_jogador == numero_aleatorio:
    print("Calculando...")
    sleep(0.7)
    print("Parabéns, você acertou!")
    sleep(0.4)
    print(f"Levou {palpites} palpites para acertar!")