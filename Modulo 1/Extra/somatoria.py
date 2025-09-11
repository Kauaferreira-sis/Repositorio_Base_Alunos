nome = input("Digite seu nome: ")
altura = float(input("Digite sua altura: "))
peso = float(input("digite seu peso: ")) 

imc = peso / (altura ** 2)

print(f"bom {nome} seu imc é: {imc:.2f}. ")

if imc < 18.5:
  print ("voce esta abaixo do peso,coma mais ")
elif imc < 25.0:
   print(" muito bem vc esta no seu peso normal")
elif imc < 29.9:
   print ("Você esta sobrepeso cuidado pode piorar! ")
elif imc <+ 34.9:
    print ("Cuidado obesidade grau 1, pode fazer uns exercicios ")
elif imc <= 39.9: 
   print("cuidado obesidade grau 2, faça uma dieta e uma academia")
else:
   print ("opa obesidade grau 3, vai participar dos kilos mortais ")
