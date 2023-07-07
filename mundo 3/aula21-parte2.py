#INTERACTIVE HELP
'''help() #<- Interactive help
print(input.__doc__)'''

#DOCSTRINGS PARA DOCUMENTAÇÃO
'''def contador(i, f, p):
    """
       -> Faz uma contagem e mostra na tela.
       :param i: início da contagem
       :param f: fim da contagem
       :param p: passo da contagem
       :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print()
    print('FIM!')


help(contador)'''

#PARAMETRO OPCIONAL
'''def somar(a = 0, b = 0, c = 0):
    s = a + b + c
    print(f'A soma dos valores vale {s}')

somar(3,2,5)
somar(8,4)
somar()'''

#ESCOPO DE VARIÁVEIS
'''#Toda variável inicializada dentro de uma função (def) ela será de escopo local
#Toda variável inicializada dentro do programa principal ela será de escopo global
#global
def teste(b):
    global a #usando esse comando é possivel mexer na variavel global dentro de uma funçao
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


a = 5
teste(a)
print(f'A fora vale {a}')'''

#RETURN
'''def somar(a = 0, b = 0, c = 0):
    s = a + b + c
    return s


r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(6)
print(f'Os resultados foram: {r1}, {r2} e {r3}')'''

##########################################################
'''def fatorial(num = 1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


#n = int(input('Digite um número: '))
#print(f'O fatorial de {n} é igual a {fatorial(n)}')
f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são: {f1}, {f2} e {f3}')'''
############################
'''def par(n = 0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('Não é par!')'''