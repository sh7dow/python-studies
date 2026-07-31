from time import sleep
from sys import exit

print("--" * 23)
sleep(0.7)
print("Bem vindo à Calculadora Python!")
sleep(0.7)
print("--" * 23)
sleep(0.5)

contador_operacao = 0
contador_primeironum = 0
contador_segundonum = 0
contador_continuacao = 0
continuar = "Y"

while continuar == "Y":
    operacao_usuario = str(
        input(
            f"Escolha uma operação: \n [1] Adição \n [2] Subtração \n [3] Multiplicação \n [4] Divisão ({contador_operacao}x) \n  "
        )
    )

    while operacao_usuario not in ["1", "2", "3", "4"]:
        contador_operacao = contador_operacao + 1
        if contador_operacao == 10:
            print("Você fez 10 solicitações inválidas! Programa fechando...")
            sleep(1)
            exit()
        operacao_usuario = str(
            input(
                f"Formatação inválida! Escolha novamente: \n [1] Adição \n [2] Subtração \n [3] Multiplicação \n [4] Divisão ({contador_operacao}x)  \n  "
            )
        )

    primeiro_numero = str(input("Diga o primeiro número da sua operação: "))
    while not primeiro_numero.isnumeric():
        contador_primeironum = contador_primeironum + 1
        if contador_primeironum == 10:
            print("Você fez 10 solicitações inválidas! Programa fechando...")
            sleep(1)
            exit()

        primeiro_numero = str(
            input(
                f"Formatação inválida! Diga novamente o primeiro número da sua operação: ({contador_primeironum}x) "
            )
        )

    segundo_numero = str(input("Diga o segundo número da sua operação: "))
    while not segundo_numero.isnumeric():
        contador_segundonum = contador_segundonum + 1
        if contador_segundonum == 10:
            print("Você fez 10 solicitações inválidas! Programa fechando...")
            sleep(1)
            exit()
        segundo_numero = str(
            input(
                f"Formatação inválida! Diga novamente o segundo número da sua operação: ({contador_segundonum}x) "
            )
        )

    primeiro_numero = int(primeiro_numero)
    segundo_numero = int(segundo_numero)
    operacao_usuario = int(operacao_usuario)

    if operacao_usuario == 1:
        print(
            f"{primeiro_numero} + {segundo_numero} = {primeiro_numero + segundo_numero}"
        )
    elif operacao_usuario == 2:
        print(
            f"{primeiro_numero} - {segundo_numero} = {primeiro_numero - segundo_numero}"
        )
    elif operacao_usuario == 3:
        print(
            f"{primeiro_numero} * {segundo_numero} = {primeiro_numero * segundo_numero}"
        )
    elif operacao_usuario == 4:

        if segundo_numero == 0:
            print("Não é possível dividir por zero!")
        else:
            resultado_divisão = primeiro_numero / segundo_numero

            if resultado_divisão == int(resultado_divisão):
                resultado_divisão = int(resultado_divisão)
                print(f"{primeiro_numero} / {segundo_numero} = {resultado_divisão}")
            else:
                print(f"{primeiro_numero} / {segundo_numero} = {resultado_divisão}")

    sleep(0.8)
    print("...")
    sleep(0.5)

    pergunta_continuar = str(
        input("Você quer continuar a fazer contas? [Y] | [N] ")
    ).upper()

    while pergunta_continuar not in ["Y", "N"]:
        contador_continuacao = contador_continuacao + 1
        if contador_continuacao == 10:
            print("Você fez 10 solicitações inválidas! Programa fechando...")
            sleep(1)
            exit()
        pergunta_continuar = str(
            input(
                f"Formatação inválida! Tente novamente: [Y] | [N] ({contador_continuacao}x) "
            )
        ).upper()

    continuar = pergunta_continuar

    if pergunta_continuar == "N":
        sleep(0.5)
        print("Obrigado pelos cálculos! Saindo do sistema...")
        sleep(0.5)
        print("...")
        sleep(0.8)
        print("...")
        sleep(0.6)
        exit()
