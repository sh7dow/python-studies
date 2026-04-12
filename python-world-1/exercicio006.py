# Criar um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

numero = int(input('Digite o seu número: '))

# Usando f-string (novo metodo), basicamente, uma substituição ao ".format", botar o f de format atras de uma string
# (aspas), faz com que você possa botar diretamente o nome das variáveis dentro das chaves {}, e não dps como o ".format"
# também da para usar o ":.2f", para mostrar só duas casas floats e não mostrar dizimas
print(f'O dobro do seu número é: {numero*2:.2f} \n O triplo é: {numero*3:.2f} \n A raiz quadrada é: {pow(numero, 1/2):.2f}')
# Para definir a raiz quadrada, é só fazer uma potência e depois 1/2.