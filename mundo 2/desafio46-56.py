import time
import datetime

################46################
'''for c in range(10, -1, -1):
    print(c)
    time.sleep(1)
print('FIM')'''
################47################
'''for c in range(2, 51, 2):
    print(c, end=' ')
print('FIM')'''
################48################
'''s = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        s += c
print(f'O somatório dos {cont} valores é de: {s}')'''
################49################
'''for a in range(1, 10):
    for b in range(1, 11):
        c = a * b
        print(f'{a} X {b} = {c}')
    print('\n')'''
'''n = int(input('Digite um numero para ver a sua tabuada: '))
for c in range(1, 11):
    print(f'{n} X {c} = {n * c}')'''
################50################
'''s = 0
for c in range(1, 7):
    n = int(input('Digite um numero inteiro: '))
    if n % 2 == 0:
        s += n
print(f'A soma dos valores pares é de {s}')'''
################51################
'''p = int(input('Qual o primeiro termo da PA? '))
r = int(input('Qual a razao dessa PA? '))
s = p + (10 - 1) * r
for c in range(p, s + r, r):
    print(f'{c} ', end='→ ')    
print('FIM')'''
################52################
'''n = int(input('Digite um numero inteiro: '))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print(f'{c}\033[m', end=' ')
print(f'\nO numero {n} foi divisivel {tot} vezes')
if tot == 2:
    print('E por isso ele é primo!')
else:
    print('E por isso ele não é primo!')'''
################53################
'''frase = str(input('Digite uma frase: ')).strip().upper()
frase = frase.replace(' ', '')
inverso = frase[::-1]
#inverso = ''
#for letra in range(len(frase) -1, -1, -1):
#    inverso += frase[letra]
print(f'O inverso de {frase} é {inverso}')
if inverso == frase:
    print('Temos um palídromo!')
else:
    print('A frase digitada não é um palídromo!')'''
################54################
'''maior = 0
menor = 0
for c in range(1, 8):
    ano = int(input(f'Digite o ano que a pessoa {c} nasceu: '))
    if datetime.date.today().year - ano < 21:
        menor += 1
    else:
        maior += 1
print(f'{menor} pessoas sao menores de idade e {maior} sao maioroes de idade')'''
################55################
'''maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input(f'Qual o peso da {p} pessoa: '))
    if p == 1:
        menor = peso
        maior = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso foi de {maior}Kg')
print(f'O menor peso foi de {menor}Kg')'''
################56################
'''count = 0
media = 0
maiorh = 0
nomevelho = ''
countm = 0
for p in range(1, 5):
    print(f'----- {p}ª PESSOA -----')
    nome = str(input('NOME: ')).strip()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO (M/F): ')).strip()
    count += idade
    if p == 1 and sexo in 'Mm':
        maiorh = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maiorh:
        maiorh = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        countm += 1
media = count / 4
print(f'A média de idade do grupo é de {media} anos!\n')
print (f'O homem mais velho do grupo é o {nomevelho} e ele tem {maiorh} anos.\n')
print(f'Existem {countm} mulher(es) no grupo com menos de 20 anos de idade.')'''