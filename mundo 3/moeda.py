def metade(valor=0, format=False):
    res = valor / 2
    if not format:
        return res
    else:
        return moeda(res)


def dobro(valor=0, format=False):
    res = valor * 2
    if not format:
        return res
    else:
        return moeda(res)


def aumentar(valor=0, por=0, format=False):
    res = valor + (valor * por/100)
    if not format:
        return res
    else:
        return moeda(res)


def diminuir(valor, por=0, format=False):
    res = valor - (valor * por/100)
    if not format:
        return res
    else:
        return moeda(res)


def moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor:>.2f}'.replace('.', ',')


def resumo(valor=0, aum=10, des=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(valor)}')
    print(f'Dobro do preço: \t{dobro(valor, True)}')
    print(f'Metade do preço: \t{metade(valor, True)}')
    print(f'{aum}% aumento do preço: \t{aumentar(valor, aum, True)}')
    print(f'{des}% desconto do preço: \t{diminuir(valor, des, True)}')
    print('-' * 30)
