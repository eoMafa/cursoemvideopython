'''def linha():
    print('-' * 40)


linha()'''
##############################################
'''def cabecalho(msg):
    print('-' * 30)
    print(msg)
    print('-' * 30)


cabecalho('SISTEMA DE ALUNOS')
cabecalho('TESTE PARA AULA')
cabecalho('MAFAGAFO É FODA')'''
##############################################
'''def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B é = {s}')


soma(3, 1)
soma(b = 4, a = 5)'''
##############################################
'''def contador(*num):
    for v in num:
        print(v, end=' ')
    print()
    print(f'Recebi os valores {num} e são ao todo {len(num)} números')


contador(4, 7, 5, 4)
contador(8, 5)
contador(2, 8, 5, 3)'''
##############################################
'''def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [7,2,5,0,4]
dobra(valores)
print(valores)'''