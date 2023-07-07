import math
import random
################72################
'''extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 
              'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 
              'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
continuar = ' '
while continuar not in 'N':
    escolha = int(input('Digite um número entre 0 e 20: '))
    if 0 <= escolha <= 20:
        print(f'Voce digitou {extenso[escolha]}')
        continuar = str(input('Deseja continuar[S/N]? ')).strip().upper()[0]
        if continuar == 'N':
            break
    else:
        print('Tente Novamente.')'''
################73################
'''brasileirao = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo',
'Atlético Mineiro', 'Atlético-PR', 'Cruzeiro', 'Botafogo', 'Santos', 'Bahia',
'Corinthians', 'Fluminense', 'Ceará', 'Vasco da Gama', 'Sport Recife', 'América-MG',
'Chapecoense', 'Vitória', 'Paraná')
print('[A]Apenas os 5 primeiros colocados.')
print('[B]Os últimos 4 colocados da tabela.')
print('[C]A lista com os times em ordem alfabética.')
print('[D]Em que posição o time da Chapecoense está.')
print('[E]Sair.')
while True:
    opc = str(input('Digite a opçao que deseja analizar: ')).strip().upper()[0]
    if opc == 'A':
        print(brasileirao[0:5])
    elif opc == 'B':
        print(brasileirao[-4:])
    elif opc == 'C':
        print(sorted(brasileirao))
    elif opc == 'D':
        print(brasileirao.index('Chapecoense') + 1)
    elif opc == 'E':
        break'''
################74################
'''tupla = (random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), 
            random.randint(0, 10), random.randint(0, 10))
print(tupla)
print(f'O maior valor na tupla é: {max(tupla)}')
print(f'O menor valor na tupla é: {min(tupla)}')'''
################75################
'''tupla = (int(input('Digite o primeiro valor: ')), 
            int(input('Digite o segundo valor: ')), 
            int(input('Digite o terceiro valor: ')), 
            int(input('Digite o quarto valor: ')))
print(f'O valor 9 apareceu {tupla.count(9)} vezes.')
if 3 in tupla:
        print(f'O primeiro 3 foi digitado na posição {tupla.index(3) + 1}')
print('Os números pares na tupla são: ', end='')
for cont in range(0, len(tupla)):
    if cont % 2 == 0:
        print(cont, end=' ')'''
################76################
'''produtos = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00,
               'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 
               22.30, 'Livro', 34.90)
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end='')
    else:
        print(f'R${produtos[pos]:>7.2f}')'''
################77################
'''palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis',
            'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
for c in palavras:
    print(f'\nNa palavra {c.upper()} temos ', end='')
    for letra in c:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')'''