senha = "arrozcomfeijao"

tentativa_usuario = str(input("Digite a senha: "))

if tentativa_usuario != str:
    tentativa_usuario

while tentativa_usuario != senha:
    print("Senha incorreta. Tente novamente!")

    tentativa_usuario = str(input("Digite a senha: "))

if tentativa_usuario == senha:
    print("Senha correta. Acesso concedido no sistema.")

