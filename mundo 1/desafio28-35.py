import random
import datetime
####################28####################
'''n = random.randint(0, 5)
usuario = int(input('Digite um numero de 0 a 5: '))
if n != usuario:
    print('Você errou! :(\n')
else:
    print(f'Parabens voce adivinhou o numero {n}!!!')'''
####################29####################
'''velo = float(input('Digite a velocidade do carro (em km/h): '))
if velo > 80:
    multa = (velo - 80) * 7
    print(f'Voce sera multado em R${multa :.2f} por estar à {velo}km/h.')
else:
    print('Velocidade permitida na estrada.')'''
####################30####################
'''numero = int(input('Digite um numero inteiro qualquer: '))
if numero % 2 == 0:
    print('Numero Par')
else:
    print('Numero Impar')'''
####################31####################
'''dis = float(input('Qual a distancia da viagem em km? '))
if dis <= 200:
    valor = dis * 0.5
    print(f'O valor da passagem é de R${valor :.2f}')
else:
    valor = dis * 0.45
    print(f'O valor da passagem é de R${valor :.2f}')'''
####################32####################
'''ano = int(input('Digite qual ano voce quer analisar: '))
if ano == 0:
    ano = datetime.date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('É ano bissexto')
else:
    print(f'O ano {ano} não é ano bissexto')'''
####################33####################
'''n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))
if n1 < n2 and n2 < n3:
    print(f'O maior numero é {n3} e o menor é {n1}')
elif n1 < n3 and n3 < n2:
    print(f'O maior numero é {n2} e o menor é {n1}')
elif n2 < n1 and n1 < n3:
    print(f'O maior numero é {n3} e o menor é {n2}')
else:
    print(f'O maior numero é {n2} e o menor é {n3}')'''
####################34####################
'''salario = float(input('Digite o valor do seu salário: R$'))
if salario > 1250:
    reajuste = salario + (salario * 0.1)
    print(f'Novo salario: R${reajuste :.2f}')
else:
    reajuste = salario + (salario * 0.15)
    print(f'Novo salario: R${reajuste :.2f}')'''
####################35####################
'''r1 = int(input('Digite valor da reta 1: '))
r2 = int(input('Digite valor da reta 2: '))
r3 = int(input('Digite valor da reta 3: '))
if abs(r2 - r3) < r1 < (r2 + r3) and abs(r1 - r3) < r2 < (r1 + r3) and abs(r1 - r2) < r3 < (r1 + r2):
    print('Pode se formar um triangulo')
else:
    print('Nao é possivel formar um triangulo')'''