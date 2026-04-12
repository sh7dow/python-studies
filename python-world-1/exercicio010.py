dinheiro_na_carteira = float(input("Quanto de dinheiro você tem na carteira? R$ "))
conversao_pro_dolar = dinheiro_na_carteira / 5.25
conversao_pro_euro = dinheiro_na_carteira / 6.09

print(f"Com R${dinheiro_na_carteira:.2f} \n Dólar: US${conversao_pro_dolar:.2f} \n Euros: €{conversao_pro_euro:.2f}")