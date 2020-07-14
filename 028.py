from random import randint
n =  int(input('Digite um numero de o a 5: '))
n1 = randint(0, 5)
if n == n1:
    print('Você acertou, Parabens!')
else:
    print('Você errou, tente novamente.')
print('O numero que o computador pensou foi {}'.format(n1))