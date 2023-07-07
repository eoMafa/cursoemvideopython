import random
import math
################57################
'''sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    print('Entrada invalida, tente novamente.')
    sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
print(f'Sexo {sexo} anotado com sucesso!')'''
################58################
'''n = random.randint(0, 10)
count = 0
usuario = int(input('Digite um numero de 0 a 10: '))
while n != usuario:
    usuario = int(input('Você errou, tente novamente :'))
    count += 1
print(f'Parabens voce adivinhou o numero {n} em {count} vezes!!!')'''
################59################
'''v1 = int(input('Digite o primeiro valor: '))
v2 = int(input('Digite o segundo valor: '))
resultado = 0
menu = 0
while menu != 5:
    print('[1]Somar\n[2]Multiplicar\n[3]Maior\n[4]Novos numeros\n[5]Sair do programa\n')
    menu = int(input('Digite a opçao desejada: '))
    if menu == 1:
        resultado = v1 + v2
        print(f'O valor da soma entre os dois valores é {resultado}')
    elif menu == 2:
        resultado = v1 * v2
        print(f'O valor da soma entre os dois valores é {resultado}')
    elif menu == 3:
        if v1 > v2:
            print('O primeiro valor é maior que o segundo')
        elif v2 > v1:
            print('O segundo valor é maior que o primeiro')
        else:
            print('Os dois valores sao iguais.')
    elif menu == 4:
        v1 = int(input('Digite o novo primeiro valor: '))
        v2 = int(input('Digite o novo segundo valor: '))
    elif menu > 5:
        print('Entrada inválida, tente novamente!')
else:
    print('Ate mais!!!!')'''
################60################
'''numero = int(input('Digite um número para calcular o fatorial: '))
f = math.factorial(numero)
print(f'O fatorial de {numero} é {f}')'''

'''numero = int(input('Escolha um numero para calcular o fatorial: '))
fat = 1
valor = numero
print(f'Calculando {numero}!...')
while numero > 0:
    fat *= numero
    print(f'{numero}', end='')
    print(' x ' if numero > 1 else f' = {fat}', end='')
    numero -= 1
print(f'\nO fatorial de {valor} é: {fat}')'''

'''fat = 1
numero = int(input('Escolha um numero para calcular o fatorial: '))
valor = numero
for c in range(numero, 1, -1):
    fat *= numero
    numero -= 1
print(f'O fatorial de {valor} é: {fat}')'''
################61################
'''p = int(input('Qual o primeiro termo da PA? '))
r = int(input('Qual a razao dessa PA? '))
termo = p
c = 1
while c <= 10:
    print(f'{termo} ', end='→ ')
    termo += r
    c += 1
print('FIM')'''
################62################
'''p = int(input('Qual o primeiro termo da PA? '))
r = int(input('Qual a razao dessa PA? '))
c = 1
termo = p
menu = 'S'
a = 0
mais = 0
while menu == 'S':
    while c <= 10:
        print(f'{termo} ', end='→ ')
        termo += r
        c += 1
    menu = str(
        input('\nDeseja continuar com a progressao? [S/N] ')).strip().upper()[0]
    if menu == 'S':
        mais = int(input('Quantos outros termos voce quer ver? '))
        while a <= mais:
            print(f'{termo} ', end='→ ')
            termo += r
            a += 1
print('FIM')'''
################63################
'''elementos = int(input('Quantos elementos voce deseja ver da sequencia de Fibonacci? '))
t1 = 0
t2 = 1
print(f'{t1} → {t2}', end='')
c = 3
while c <= elementos:
    t3 = t2 + t1
    print(f' → {t3}', end='')
    t1 = t2
    t2 = t3
    c += 1
print('\nFIM')'''
################64################
'''numero = count = soma = 0
numero = int(input('Digite um número: '))
while numero != 999:
    soma += numero
    count += 1
    numero = int(input('Digite um número: '))
print(f'Foram digitados {count} numeros e a soma foi de {soma}')'''
################65################
'''continuar = 'S'
count = media = soma = maior = menor = 0
while continuar == 'S':
    numero = int(input('Digite um número: '))
    soma += numero
    count += 1
    if count == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    continuar = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
media = soma / count
print(f'A média dos {count} numeros foi de {media}')
print(f'O maior valor foi {maior} e o menor valor foi {menor} ')'''