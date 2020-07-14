nome = str(input('Qual o seu nome? ')).strip()
minu= nome.lower()
maiu = nome.upper()
espa = len(nome.replace(" ", ""))
letr = nome.split()[0]
apa = len(letr)
print('O seu nome completo é: {}\nCom todas as letras maiscúlas fica: {}\nE com todas minúscula fica: {}'.format(nome, maiu, minu))
print('Seu nome completo tem {} letras\nE o primeiro nome é {}\nSeu primeiro nome tem {} letras'.format(espa, letr, apa))