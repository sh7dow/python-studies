# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de
# tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de dois metros quadrados

largura = float(input('Quanto de largura tem a parede? '))
altura = float(input('Quanto de altura tem a parede? '))

area = largura * altura
tinta = area / 2

print(f"A parede tem a dimensão de {largura}x{altura} e sua área é de {area}m²")
print(f"Para pintar essa parede de {area}m², você precisará de {tinta}L de tinta.")
