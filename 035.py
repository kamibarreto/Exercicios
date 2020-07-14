lin1 = float(input('Digite o comprimento da primeira reta: '))
lin2 = float(input('Digite o comprimento da segunda reta: '))
lin3 = float(input('Digite o comprimento da terceira reta: '))
if lin1 < lin2 + lin3:
    if lin2 < lin1 + lin3:
        if lin3 < lin1 + lin2:
            print('Essas retas podem formar um tringulo')
        else:
            print('Não pode ser um triangulo.')
    else:
        ('Não pode ser um triangulo.')
else:
    print('Não pode ser um triangulo.')