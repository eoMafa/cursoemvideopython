import math
import random
import time
import operator
import datetime
################90################
'''aluno = {}
aluno['Nome'] = str(input('Nome: ')).strip().lower().capitalize()
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
if aluno['Média'] >= 6.0:
    aluno['Situação'] = 'Aprovado'
else:
    aluno['Situação'] = 'Reprovado'
for k, v in aluno.items():
    print(f'O {k} é igual a {v}')'''
################91################
'''dado = {'Dado 1': random.randint(1, 6), 'Dado 2': random.randint(1, 6),
        'Dado 3': random.randint(1, 6), 'Dado 4': random.randint(1, 6)}
rank = []
for k, v in dado.items():
    print(f'O {k} tirou {v}')
    time.sleep(1)
rank = sorted(dado.items(), key=operator.itemgetter(1), reverse=True)
for i, v in enumerate(rank):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')'''
################92################
'''trabalhador = {}
trabalhador['Nome'] = str(input('Nome: ')).strip().lower().capitalize()
nascimento = int(input('Ano de nascimento: '))
trabalhador['Idade'] = datetime.date.today().year - nascimento
trabalhador['CTPS'] = int(input('Digite a Carteira de Trabalho (0 p/ não tem): '))
if trabalhador['CTPS'] != 0:
    trabalhador['Contrato'] = int(input('Ano de contratação: '))
    trabalhador['Salario'] = float(input('Salário: R$'))
    trabalhador['Aposenta'] = datetime.date.today().year - trabalhador['Contrato']
print(trabalhador)
for k, v in trabalhador.items():
    print(f'{k} tem valor {v}')'''
################93################
'''jogador = {}
total = 0
jogador['Nome'] = str(input('Nome: ')).strip().lower().capitalize()
jogador['Partidas'] = int(input('Número de partidas: '))
for c in range(0, jogador['Partidas']):
    jogador['Gols'] = int(input(f'{c + 1}º partida: '))
    total += jogador['Gols']
jogador['Total'] = total
print(jogador)'''

'''jogador = {}
partidas = []
jogador['Nome'] = str(input('Nome: ')).strip().lower().capitalize()
total = int(input(f'Quantas partidas o jogador {jogador["Nome"]} jogou? '))
for p in range(0, total):
    partidas.append(int(input(f'Quandos gols na {p + 1}º partida? ')))
jogador['Gols'] = partidas[:]
jogador['Total'] = sum(partidas)
for k, v in jogador.items():
    print(f'O {k} tem o valor {v}')
print(f'O jogador {jogador["Nome"]} jogou {len(jogador["Gols"])} partidas.')
for i, v in enumerate(partidas):
    print(f'Na partida {i + 1} ele fez {v} gols')
print(f'Total de gols: {jogador["Total"]}.')'''
################94################
'''galera = []
pessoa = {}
soma = media = 0
while True:
    pessoa.clear()
    pessoa['Nome'] = str(input('Nome: ')).strip().lower().capitalize()
    while True:
        pessoa['Sexo'] = str(input('Sexo[M/F]: ')).strip().upper()[0]
        if pessoa['Sexo'] in 'MF':
            break
        print('ERRO! Digite apenas M ou F.')
    pessoa['Idade'] = int(input('Idade: '))
    soma += pessoa['Idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar[S/N]? ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('Por favor, digite apenas S ou N.')
    if resp == 'N':
        break
media = soma / len(galera)
print(f'Ao todo temos {len(galera)} pessoas cadastradas.')
print(f'A média de idade das pessoas é {media:5.2f} anos.')
print('As mulheres cadastradas foram: ', end='')
for p in galera:
    if p['Sexo'] == 'F':
        print(f'{p["Nome"]}', end=' ')
print()
print('Lista das pessoas com idade acima da média: ', end='')
for p in galera:
    if p['Idade'] >= media:
        print('   ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('ENCERRADO')'''
################95################
'''jogador = {}
partidas = []
time = []
while True:
    jogador.clear()
    jogador['Nome'] = str(input('Nome: ')).strip().lower().capitalize()
    total = int(input(f'Quantas partidas o jogador {jogador["Nome"]} jogou? '))
    partidas.clear()
    for p in range(0, total):
        partidas.append(int(input(f'Quandos gols na {p + 1}º partida? ')))
    jogador['Gols'] = partidas[:]
    jogador['Total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        res = str(input('Deseja continuar[S/N]? ')).strip().upper()[0]
        if res in 'SN':
            break
        print('Opção inválida. Digite apenas S ou N')
    if res == 'N':
        break
print('-=' * 30)
print('Cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dado de qual jogador? (999 p/ parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print('Erro! Codigo nao existe.')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["Nome"]}: ')
        for i, g in enumerate(time[busca]['Gols']):
            print(f'    No jogo {i+1} fez {g} gols')
    print('-' * 40)
print('<<ENCERRADO>>')'''