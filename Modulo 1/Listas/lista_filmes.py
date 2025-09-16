print ("Digite 3 filmes para adicionar a lista  ")

cont = 1
filmes = []
while cont <= 3  : 
    nome = (input(f"digite o {cont}° filme: "))
    filmes.append(nome)
    cont += 1

print(filmes)