import math
import datetime
import time
################101################
'''def voto(num):
    v = datetime.date.today().year - num
    if v < 16:
        print(f'Com {v} anos não pode votar!')
    elif 18 <= v <= 65:
        print(f'Com {v} anos o voto é obrigatório!')
    else:
        print(f'Com {v} anos o voto é opcional!')


print('-' * 30)
ano = int(input('Em que ano você nasceu: '))
voto(ano)'''
################102################
'''def fatorial(num = 1, show = False):
    """
        ->Calcula o fatorial de um número.
        :param n: O número a ser calculado.
        :param show: (opcional) Mostrar ou não a conta.
        :return: O valor do fatorial de um número n.
    """
    f = 1
    for c in range(num, 0, -1):
        f *= c
    if show == True:
        for c in range(num, 0, -1):
            if c == 1:
                print(f'{c} = ', end='')
            else:
                print(f'{c} x ', end='')
        return f
    else:
        return f


print(fatorial(5, True))
help(fatorial)'''
################103################
'''def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


print('-' * 30)
n = str(input('Qual o nome do jogador? '))
g = str(input(f'Quantos gols o jogador {n} fez? '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gols = g)
else:
    ficha(n, g)'''
################104################
'''def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mErro! Digite um número válido.\033[m')
        if ok:
            break
    return valor


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')'''
################105################
'''def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: Uma ou mais notas dos alunos (aceita várias).
    :param sit: Valor opcional, indicando se deve ou não adicionar a situação.
    :return: Dicionário com várias informações sobre a situação da turma.
    """
    r = {}
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Média'] = sum(n)/len(n)
    if sit:
        if r['Média'] >= 7:
            r['Situação'] = 'BOA'
        elif r['Média'] >= 5:
            r['Situação'] = 'RAZOÁVEL'
        else:
            r['Situação'] = 'RUIM'
    return r


resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
help(notas)'''
################106################
'''c = ('\033[m',        # 0 - sem cor
     '\033[0;30;41m',  # 1 - vermelho
     '\033[0;30;42m',  # 2 - verde
     '\033[0;30;43m',  # 3 - amarelo
     '\033[0;30;44m',  # 4 - azul
     '\033[0;30;45m',  # 5 - roxo
     '\033[7;30m'     # 6 - branco
     )


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    time.sleep(2)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    time.sleep(1)


# Programa principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input("Função ou Biblioteca > "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 1)
'''