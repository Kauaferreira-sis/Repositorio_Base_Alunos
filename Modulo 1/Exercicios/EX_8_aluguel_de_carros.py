# Aluguel de carros:
# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado
# Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0.15 por km rodado

# OUTPUT ESPERADO:

# Por quantos dias o carro foi alugado: 10
# Quantos km o carro rodou: 500
# Você andou 500.0km por 10 dias, então o preço a pagar é R$675.00.

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

dias = int(input("por quantos dias o carro foi alugado: "))
km = float(input("quantos km o carro rodou: "))

valor_dias = dias * 60
valor_km =  km * 0.15
valor_total = valor_dias + valor_km
print(f"voce andou {km}km por dias, então o preço a pagar é R$: {valor_total}")