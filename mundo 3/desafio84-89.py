import math
import random
import time
################84################
'''lista = []
temp = []
maior = menor = 0
while True:
    temp.append(str(input('Digite o nome da pessoa: ')).strip().lower().capitalize())
    temp.append(float(input('Digite o peso dessa pessoa[Kg]: ')))
    if len(lista) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    lista.append(temp[:])
    temp.clear()
    cont = str(input('Deseja continuar[S/N]? ')).strip().upper()[0]
    if cont in 'N':
        break
print(f'Existem {len(lista)} pessoas!')
print(f'O menor peso é o: {menor:.2f}Kg. Peso de ', end='')
for p in lista:
    if p[1] == menor:
        print(f'[{p[0]}]', end='')
print()
print(f'O maior peso é o: {maior:.2f}Kg. Peso de ', end='')
for p in lista:
    if p[1] == maior:
        print(f'[{p[0]}]')'''
################85################
'''num = [[], []]
for c in range(1, 8):
    valor = (int(input(f'Digite o {c}º valor: ')))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
num[0].sort()
num[1].sort()
print(f'A lista é: {num}')
print(f'Os valores pares sao os {num[0]}')
print(f'Os valores impares sao os {num[1]}')'''
################86################
'''matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()'''
################87################
'''matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = terceira = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]
    print()
for l in range(0, 3):
    terceira += matriz[l][2]
for c in range(0, 3):
    if c == 0:
        maior = c
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'A soma dos valores pares é de: {soma}')
print(f'A soma dos valores da terceira coluna é de: {terceira}')
print(f'O maior valor da segunda linha é: {maior}')'''
################88################
'''lista = []
jogos = []
print('-' * 30)
print('      JOGA NA MEGA SENA DA VIRADA      ')
print('-' * 30)
quant = int(input('Quantos jogos deseja simular? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = random.randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f'SORTEANDO {quant} JOGOS', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i + 1}: {l}')
    time.sleep(1)
print('-=' * 5, '< BOA SORTE CARALHOO! >', '-=' * 5)'''
################89################
'''ficha = []
while True:
    nome = str(input('Nome: ')).strip().lower().capitalize()
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    ficha.append([nome, [n1, n2], media])
    cont = str(input('Deseja continuar[S/N]? ')).strip().upper()[0]
    if cont in 'N':
        break
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 30)
    opc = int(input('Mostrar as notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')'''