pro = float(input('Qual o preço do produto: R$'))
porce = pro * 0.05
descon = pro - porce
print('Seu produto custa R${:.2f}, com 5% de desconto ficara R${:.2f}'.format(pro, descon))
print('Tendo seu desconto de R${:.2f}'.format(porce))