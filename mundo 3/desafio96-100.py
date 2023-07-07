import math
import time
import random
################96################
'''def cabecalho():
    print('-' * 30)
    print('     ÁREA DE UM TERRENO      ')
    print('-' * 30)

def area(l, c):
    a = l * c
    print(f'A área do terreno de largura {l} e comprimento {c} é: {a:.2f}')


cabecalho()
l = float(input('Qual a largura do terreno? '))
c = float(input('Qual o comprimento do terreno? '))
area(l, c)'''
################97################
'''def escreva(msg):
    print('-' * (len(msg) + 4))
    print(f'  {msg}')
    print('-' * (len(msg) + 4))


escreva('Teste de texto')'''
################98################
'''def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}:')
    time.sleep(1)
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            time.sleep(0.5)
            cont += p
        print()
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            time.sleep(0.5)
            cont -= p
        print()
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)'''
################99################
'''def maior(*num):
    maior = 0
    print('-=' * 30)
    print('Analisando valores passados...')
    time.sleep(1)
    for i, v in enumerate(num):
        if i == 0:
            maior = v
        if maior < v:
            maior = v
        print(f'{v}', end=' ')
    print()
    print(f'Foram analisados {len(num)} ao todo.')
    print(f'O maior número analisado é: {maior}')


maior(7, 4, 5, 8, 9)
maior(1, 4, 6)
maior(7, 2, 0, 10, 22, 64)
maior()'''
################100################
'''def sorteia():
    print('Sorteando os valores...')
    time.sleep(1)
    for c in range(0, 5):
        numeros.append(random.randint(0, 10))
        print(numeros[c], end=' ')
        time.sleep(0.5)
    print()
    print('PRONTO!')

def sorteiapar(lst):
    soma = 0
    for v in lst:
        if v % 2 == 0:
            soma += v
    print(f'A soma dos valores pares de {lst} é: {soma}')


numeros = []
sorteia()
time.sleep(1)
sorteiapar(numeros)'''
