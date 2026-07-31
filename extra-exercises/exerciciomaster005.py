idade_acumulador = 0
idade_acumulador_maior = 0
idade_acumulador_menor = 0
idade_acumulador_mulher_20 = 0
idade_acumulador_homem_25 = 0
mulheres_acumulador = 0
homens_acumulador = 0
abaixo_peso_acumulador = 0
peso_ideal_acumulador = 0
sobrepeso_acumulador = 0
obesidade_acumulador = 0
obesidade_morbida_acumulador = 0


for pessoa in range(1, 6):
    nome = str(input("Qual é o seu nome? "))
    idade = int(input("Qual sua idade? "))
    sexo = str(input("Qual seu sexo? [M/F] ")).lower().strip()
    cidade = str(input("Qual sua cidade? "))
    peso = float(input("Qual seu peso? "))
    altura = float(input("Qual sua altura? "))

    idade_acumulador = idade_acumulador + idade
    media = idade_acumulador / 5
    imc = peso / (altura * altura)

    if pessoa == 1:
        idade_maior = idade
        idade_menor = idade
        nome_maior = nome
        nome_menor = nome
    else:
        if idade > idade_maior:
            idade_maior = idade
            nome_maior = nome
        if idade < idade_menor:
            idade_menor = idade
            nome_menor = nome
    if sexo == 'm':
        homens_acumulador = homens_acumulador + 1
    if sexo == 'f':
        mulheres_acumulador = mulheres_acumulador + 1

    if idade >= 18:
        idade_acumulador_maior = idade_acumulador_maior + 1

    elif idade < 18:
        idade_acumulador_menor = idade_acumulador_menor + 1

    if sexo == 'f' and idade < 20:
        idade_acumulador_mulher_20 = idade_acumulador_mulher_20 + 1

    if sexo == 'm' and idade > 25:
        idade_acumulador_homem_25 = idade_acumulador_homem_25 + 1

    if pessoa == 1:
        peso_maior = peso
        peso_menor = peso
    else:
        if peso > peso_maior:
            peso_maior = peso
        if peso < peso_menor:
            peso_menor = peso

    if pessoa == 1:
        maior_imc = imc
        menor_imc = imc
    else:
        if imc > maior_imc:
            maior_imc = imc
        if imc < menor_imc:
            menor_imc = imc

    if imc < 18.5:
        abaixo_peso_acumulador = abaixo_peso_acumulador + 1
    elif imc < 25:
        peso_ideal_acumulador = peso_ideal_acumulador + 1
    elif imc < 30:
        sobrepeso_acumulador = sobrepeso_acumulador + 1
    elif imc < 40:
        obesidade_acumulador = obesidade_acumulador + 1
    else:
        obesidade_morbida_acumulador = obesidade_morbida_acumulador + 1

print(f"A média de idade é {media}")
print(f"A pessoa mais velha é {nome_maior} com {idade_maior} ano(s).")
print(f"A pessoa mais nova é {nome_menor} com {idade_menor} ano(s).")
print(f"Existe {homens_acumulador} homens.")
print(f"Existe {mulheres_acumulador} mulheres.")
print(f"Tem {idade_acumulador_maior} pessoas com mais ou 18 anos de idade.")
print(f"Tem {idade_acumulador_menor} pessoas com menos de 18 anos de idade.")
print(f"Tem {idade_acumulador_mulher_20} mulheres com menos ou 20 anos de idade.")
print(f"Tem {idade_acumulador_homem_25} homens com 25 anos ou mais")
print(f"O maior peso do grupo é {peso_maior}")
print(f"O menor peso do grupo é {peso_menor}")
print(f"O maior IMC do grupo é {maior_imc:.2f}")
print(f"O menor IMC do grupo é {menor_imc:.2f}")
print(f"Tem {abaixo_peso_acumulador} pessoa(s) abaixo do peso.")
print(f"Tem {peso_ideal_acumulador} pessoa(s) com o peso ideal.")
print(f"Tem {sobrepeso_acumulador} pessoa(s) com sobrepeso.")
print(f"Tem {obesidade_acumulador} pessoa(s) obesas.")
print(f"Tem {obesidade_morbida_acumulador} pessoa(s) com obesidade mórbida.")
