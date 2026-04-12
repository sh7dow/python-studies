temperatura_celsius = float(input("Informe a temperatura em °C: "))
conversao_celsius_pra_fahrenheit = 9 * temperatura_celsius / 5 + 32 # <----- Segundo a ordem de precedência, pode ser feito sem parenteses.

print(f"{temperatura_celsius:.1f}°C convertido em °F é: {conversao_celsius_pra_fahrenheit:.1f}°F")
