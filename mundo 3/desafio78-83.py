import math
################78################
'''valores = []
for c in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
for pos, c in enumerate(valores):
    if pos == 0:
        menor = maior = c
        pmaior = pmenor = pos
    if menor > c:
        menor = c
        pmenor = pos
    if maior < c:
        maior = c
        pmaior = pos
print(f'O menor valor é {menor} e esta na posiçao {pmenor}!')
print(f'O maior valor é {maior} e esta na posiçao {pmaior}!')'''
################79################
'''valores = []
cont = ' '
while True:
    n = int(input('Digite um valor: '))
    if n not in valores:
        valores.append(n)
        print('Valor adicionado!')
    else:
        print('Valor duplicado!')
    cont = str(input('Deseja continuar[S/N]? ')).strip().upper()[0]
    if cont in 'N':
        break
valores.sort()
print(valores)'''
################80################
'''valores = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > valores[-1]:
        valores.append(n)
    else:
        pos = 0
        while pos < len(valores):
            if n <= valores[pos]:
                valores.insert(pos, n)
                break
            pos += 1
print(f'Os valores digitados em ordem foram: {valores}')'''
################81################
'''valores = []
cont = ' '
while True:
    valores.append(int(input('Digite um valor: ')))
    cont = str(input('Deseja continuar[S/N]? ')).strip().upper()[0]
    if cont in 'N':
        break
print(f'Foram digitados {len(valores)} numeros')
valores.sort(reverse=True)
print(f'A lista de forma decrescente é: {valores}')
if 5 in valores:
    print('O numero 5 está na lista!')
else:
    print('O numero 5 nao está na lista!!')'''
################82################
'''valores = []
par = []
impar = []
while True:
    valores.append(int(input('Digite um valor: ')))
    cont = str(input('Deseja continuar[S/N]? ')).strip().upper()[0]
    if cont in 'N':
        break
# par = valores[:]
# impar = valores[:]
# for c in par:
#    if c % 2 == 1:
#        par.remove(c)
# for c in impar:
#    if c % 2 == 0:
#        impar.remove(c)
for c in valores:
    if c % 2 == 0:
        par.append(c)
    else:
        impar.append(c)
print(f'A lista original é {valores}')
print(f'Os numeros pares na lista são: {par}')
print(f'Os numeros ímpares na lista são: {impar}')'''
################83################
'''ex = str(input('Digite a expressao: '))
expressao = []
for c in ex:
    if c == '(':
        expressao.append('(')
    elif c == ')':
        if len(expressao) > 0:
            expressao.pop()
        else:
            expressao.append(')')
            break
if len(expressao) == 0:
    print('Sua expressao esta valida!')
else:
    print('Sua expressao nao é valida')'''

'''expressao = list(str(input('Digite a expressao: ')))
abre = fecha = 0
for c in expressao:
    if c == '(':
        abre += 1
    if c == ')':
        fecha += 1
if abre - fecha != 0:
    print('Sua expressao esta errada!')
else:
    print('Sua expressao é valida!')'''