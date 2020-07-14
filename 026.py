frase = str(input('Digite uma frase: ')).strip()
up = frase.upper()
n = up.count('A')
n2 = up.find('A')
n3 = up.rfind('A')
#"r" de rigth (direita), mostra o "a" a direita, e a esquerda é o automatico
print(40 * "-")
print("A letra 'A' aparece {}\nNa cadeia a letra 'A' aparece a primeira vez na pocisão {}".format(n, n2))
print("E a letra 'A' aparece na cadeia pela ultima vez na posição {}".format(n3))
