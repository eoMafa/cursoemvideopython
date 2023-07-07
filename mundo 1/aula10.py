'''tempo = int(input('Quantos anos tem seu carro? '))
if tempo <= 3:
    print('Seu carro está novo!!')
else:
    print('Você precisa trocar de carro!')
print('--FIM--')'''

#tempo = int(input('Quantos anos tem seu carro? '))
#print('Seu carro está novo!!' if tempo <= 3 else 'Você precisa trocar de carro!')
#print('--FIM--')

'''nome = str(input('Qual o seu nome? '))
if nome == 'Mafa':
    print('Oi seu gatao!')
else:
    print('Nem eh tao gatao...')
print(f'Bom dia, {nome}')'''

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n = (n1 + n2) / 2
print(f'Sua nota é {n}')
if n >= 6:
    print('Aprovado!')
else:
    print('Reprovado!')