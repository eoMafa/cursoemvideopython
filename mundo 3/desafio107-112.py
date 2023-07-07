import moeda
import utilidadesCeV.moeda  # from utilidadesCeV import moeda
import utilidadesCeV.dado
################107################
'''p = float(input('Digite o preço: '))
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(p, 13)}')'''
################108################
'''p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'Reduzindo 13%, temos {moeda.moeda(moeda.diminuir(p, 13))}')'''
################109################
'''p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10, True)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(p, 13, True)}')'''
################110###############
'''p = float(input('Digite o preço: R$'))
moeda.resumo(p, 15, 8)'''
################111################
'''p = float(input('Digite o preço: R$'))
utilidadesCeV.moeda.resumo(p, 15, 8)'''
################112################
'''p = utilidadesCeV.dado.leiaDinheiro('Digite o preço: R$')
moeda.resumo(p, 35, 22)'''
