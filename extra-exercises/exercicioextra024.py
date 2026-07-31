numero_escolhido = 9
tentativas = 1

numero_usuario = int(input("Escolha um número: "))

if numero_usuario == 9:
    print(f"Parabéns, você acertou com {tentativas} tentativa!")
    
elif numero_usuario > 10:
    print("Tente novamente.")

elif numero_usuario < 1:
    print("Tente novamente.")

while numero_usuario != numero_escolhido:
    numero_usuario = int(input("Escolha um número: "))

    if numero_usuario > 10:
        print("Número inválido, tente novamente.")
      
    elif numero_usuario < 1:
        print("Número inválido, tente novamente.")

    else:
        tentativas = tentativas + 1

    if numero_usuario == numero_escolhido:
        print(f"Parabéns! Você acertou o número, levou {tentativas} tentativas para conseguir acertar.")
    
