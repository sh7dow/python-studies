
nome = str(input("Nome do cadastro: ")).strip()
nomemaiusculo = nome.upper()
nomeminusculo = nome.lower()
nomeletrasaotodo = len(nome) - nome.count(" ")
nomeprimeironome = len(nome.split()[0])

print("O nome com todas as letras maiúsculas é: \n", nomemaiusculo)
print("O nome com todas as letras minúsculas é: \n", nomeminusculo)
print("A quantidade de letras que o nome tem sem espaços é: \n ", nomeletrasaotodo)
print("A quantidade de letras do primeiro nome é: \n", nomeprimeironome)