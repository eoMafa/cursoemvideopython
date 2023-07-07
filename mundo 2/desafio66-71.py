import math
import random

################66################
'''s = qtd = 0
while True:
    n = int(input('Digite um valor para n (999 para parar): '))
    if n == 999:
        break
    s += n
    qtd += 1
print(f'Foram digitados {qtd} números e a soma deles é de {s}!')'''
################67################
'''while True:
    n = int(input('Escolha um numero para ver sua tabuada: '))
    if n < 0:
        break
    print('-' * 30)
    for c in range(1, 11):
        print(f'{n} X {c} = {n * c}')
    print('-' * 30)
print('Programa finalizado com sucesso!')'''
################68################
'''count = 0
while True:
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou impar? ')).strip().upper()[0]
    n = int(input('Escolha um valor para jogar par ou impar: '))
    c = random.randint(0, 10)
    s = n + c
    if escolha == 'P':
        if s % 2 == 0:
            print('Voce ganhou!!!')
            print(f'Voce escolheu {n} e a maquina escolheu {c}!')
        else:
            print('Que pena!')
            print(f'Voce escolheu {n} e a maquina escolheu {c}!')
            break
    elif escolha == 'I':
        if s % 2 == 0:
            print('Que pena!')
            print(f'Voce escolheu {n} e a maquina escolheu {c}!')
            break
        else:
            print('Voce ganhou!!!')
            print(f'Voce escolheu {n} e a maquina escolheu {c}!')
    count += 1
print(f'Parabéns, voce ganhou {count} vezes seguidas!')'''
################69################
'''maior = h = m = 0
while True:
    idade = int(input('Digite a idade da pessoa: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo da pessoa[M/F]: ')).strip().upper()[0]
    if idade >= 18:
        maior += 1
    if sexo == 'M':
        h += 1
    if sexo == 'F' and idade < 20:
        m += 1
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    if cont == 'N':
        break
print(f'{maior} pessoa(s) maior(es) de idade\n{h} homem(ns)\n{m} mulher(es) com menos de 20 anos')'''
################70################
'''contador = barato = total = caros = 0
nomebarato = ''
while True:
    nome = str(input('Digite o nome de um produto: ')).strip().lower().capitalize()
    valor = float(input('Qual o valor do produto: R$'))
    contador += 1
    total += valor
    if valor > 1000:
        caros += 1
    if contador == 1 or valor < barato:
        barato = valor
        nomebarato = nome
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    if cont == 'N':
        break
print(f'O total gasto foi de R${total:.2f}!\nForam comprados {contador} produtos.\n{caros} produto(s) custa(m) mais de mil reais.\nO produto mais barato é o {nomebarato}!')'''
################71################
'''cin = vin = dez = um = 0
while True:
    valor = int(input('Qual o valor que voce deseja sacar? R$'))
    cin = valor // 50
    resto = valor % 50
    if resto < 50:
        vin = resto // 20
        resto = resto % 20
        if resto < 20:
            dez = resto // 10
            resto = resto % 10
            if resto < 10:
                um = resto // 1
                resto = resto % 1
                if resto == 0:
                    break
total = cin * 50 + vin * 20 + dez * 10 + um
print(f'Voce sacou R${total}!')
print(f'{cin} nota(s) de R$50\n{vin} nota(s) de R$20\n{dez} nota(s) de R$10\n{um} nota(s) de R$1')'''

'''valor = int(input('Qual valor voce deseja sacar? R$'))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
'''