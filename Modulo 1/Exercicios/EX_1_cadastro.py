# Escreva um programa que pede ao usuário o nome, idade, e-mail e senha para um cadastro e depois exiba as informações na tela:

# OUTPUT ESPERADO:

# | ------------------------------ |
# | ---------- CADASTRO ---------- |
# | ------------------------------ |
# | Nome: Maria
# | Idade: 17
# | Email: maria@email.com
# | Senha: 123123

# | ------------------------------ |
# | ----- USUÁRIO CADASTRADO ----- |
# | Seja bem vindo(a) Maria!
# | Email: maria@email.com
# | ------------------------------ |

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------
 

barra = f"| {30 * "_"} | "
print(barra)
print("|_____________CADASTRO___________|")
print(barra)
nome = input("| digite seu nome: ")
idade = input("| digite sua idade: ")
email = input("| digite seu email: ")
senha = input("| digite sua senha: ")


print(barra)
print("|_______USUÁRIO CADASTRADO________|")
print(barra)
print(f"| seja bem vindo(a) {nome}")
print(F"| seu email: {email}")
print(barra)