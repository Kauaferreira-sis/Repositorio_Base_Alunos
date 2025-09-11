# Atualize o código do exercício de conversor de dollar para real. Agora um "MENU" de opções aparecerá na tela pedindo ao usuário que escolha se quer converter
# de Reais para Dollar ou Dollar para reais. O usuário deve digitar a opção antes de informar os valores.

# OUTPUT ESPERADO:

#------- Exemplo 1 (Dólares para Reais):

# Escolha uma opção: 
# 1 - Dollar para Real
# 2 - Real para dollar
# Digite a opção: 1
# Informe a cotação atual do Dollar: 5.65
# Informe a quantidade de dólares: 150 
# O valor em reais é R$847.50

#---------- Exemplo 2 (Reais para Dólares)

# Escolha uma opção: 
# 1 - Dollar para Real
# 2 - Real para dollar
# Digite a opção: 2
# Informe a cotação atual do Dollar: 5.65
# Informe a quantidade de reais: 150
# O valor em dólares é $26.55

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

print("escolha uma opção")
print("1 - dollar para real")
print("2 - real para dollar")
opcao = int(input("digite a opção: "))
cotacao = float(input("informe a cotação atual do dollar: "))

if opcao == 1:
    qt_dolares = float(input("informe a quantidade de dólares: "))
    print(f"o valor em reais e R${qt_dolares * cotacao}")

elif opcao == 2:
    qt_reais = float(input("informe a quantidade de reaís: "))
    print(f"o valor em dólares e ${qt_reais / cotacao}")

else: 
    print ("opção errada")