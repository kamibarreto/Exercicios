nome = str(input("Digite seu nome: ")).strip()
n = nome.split()
n0 = n[0]
n1 = len(n) - 1
n2 = n[n1]
print('Primeiro nome: {}\nUltimo nome: {}'.format(n0, n2))