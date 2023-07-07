import urllib
import urllib.request
################113################
'''def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Por favor digite um inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\nO usuário preferiu não informar os dados.')
            return 0
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            f = float(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Por favor digite um inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[0;31mO usuário preferiu não informar os dados.\033[m')
            return 0
        else:
            return f


n = leiaInt('Digite um número inteiro: ')
f = leiaFloat('Digite um número real: ')
print(f'Você digitou os números {n} e {f}')'''
################114################
'''try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print(f'\033[0;31mO site requisitado está indisponível!\033[m')
else:
    print('Site disponível!')'''

