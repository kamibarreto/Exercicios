from random import randint
from time import sleep
n =  int(input('Digite um numero de o a 5: '))
print('PROCESSANDO...')
sleep(4)
n1 = randint(0, 5)#Faz o computador "pensar"
if n == n1:
    print('Você acertou, Parabens!')
else:
    print('Você errou, tente novamente.')
print('O numero que o computador pensou foi {}'.format(n1))