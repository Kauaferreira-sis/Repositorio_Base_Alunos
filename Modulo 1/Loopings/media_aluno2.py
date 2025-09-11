provas = int (input("Quantas provas o aluno realizou: "))

cont = 1
soma = 0
while cont <= provas : 
    nota = float(input(f"digite a nota da prova {cont}: "))
    soma = soma + nota
    cont += 1

media = soma/provas
print (f"a soma é: {media}")