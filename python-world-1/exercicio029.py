velocidade_carro = float(input("Qual é a velocidade do carro? "))

if velocidade_carro > 80:
    excesso = velocidade_carro - 80
    multa = excesso * 7
    print(f"Devido você ter passado {excesso} km, você foi multado por {multa:.2f}R$")
else:
    print("Você está na velocidade adequada!")

