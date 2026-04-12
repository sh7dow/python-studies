from random import choice

jogador = str(input("Pedra, papel ou tesoura? ")).strip().lower()

opcoes = ['pedra', 'papel', 'tesoura']
computador = choice(opcoes)

print(f"Você escolheu {jogador}.")
print(f"O computador escolheu {computador}.")

if jogador == computador:
    print("Empate.")
elif jogador == 'pedra' and computador == 'tesoura':
    print("Você venceu.")
elif jogador == 'papel' and computador == 'pedra':
    print("Você venceu.")
elif jogador == 'tesoura' and computador == 'papel':
    print("Você venceu.")
elif jogador != 'pedra' and jogador != 'papel' and jogador != 'tesoura':
    print("Jogada inválida.")
else:
    print("O computador venceu.")
