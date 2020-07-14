from random import sample
n1 = str(input("Primeiro aluno: "))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
aluno = [n1, n2, n3, n4]
sequencia = sample(aluno, k=4)
print("A sequencia a ser apresentada é:{}".format(sequencia))

