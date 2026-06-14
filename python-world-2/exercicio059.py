from time import sleep

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

opcao = 0

while opcao != 5:
    print("[1] Somar")
    print("[2] Multiplicar")
    print("[3] Maior")
    print("[4] Novos Números")
    print("[5] Sair do Programa")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        soma = n1 + n2
        print(f"A soma de seus dois valores é: {soma}")
    elif opcao == 2:
        multiplicacao = n1 * n2
        print(f"A multiplicação de seus dois valores é: {multiplicacao}")
    elif opcao == 3:
        if n1 > n2:
            maior = n1
            menor = n2
        elif n2 > n1:
            maior = n2
            menor = n1
        else:
            print("Os dois números são iguais.")
            maior = n1
            menor = n2

        print(f"O maior número é: {maior}")
        print(f"O menor número é: {menor}")

    elif opcao == 4:
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))

    elif opcao == 5:
        print("Saindo do programa...")
        sleep(0.5)
        print("...")

    else:
        print("Opção inválida, tente novamente...")
        sleep(0.6)