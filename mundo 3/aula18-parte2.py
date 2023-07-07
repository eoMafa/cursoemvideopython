'''dados = []
pessoas = []
dados.append('Mafa')
dados.append('27')
pessoas.append(dados[:])
print(pessoas[0][0])
print(pessoas[0][1])
print(dados)'''

'''teste = []
teste.append('Mafa')
teste.append('27')
print(teste)
galera = []
galera.append(teste[:])
print(galera)
teste[0] = 'Maria'
teste[1] = '22'
galera.append(teste[:])
print(galera)'''

'''galera = [['Joao', 19], ['Ana', 33], ['Joaquim', 13],
          ['Maria', 45]]
print(galera[0][0])
print(galera[1][0])
print(galera[-1][-1])
for p in galera:
    print(p[0],p[1])'''

'''galera = []
dado = []
totemai = totemen = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')).strip().lower().capitalize())
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totemai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totemen += 1'''