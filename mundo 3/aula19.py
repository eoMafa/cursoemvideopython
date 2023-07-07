#dados = {}
#dados = dict()
#dados = {'Nome': 'Pedro', 'Idade': 25}
# print(dados['Nome'])
#del dados['Idade']

'''filme = {'Titulo': 'Star Wars', 
         'Ano': 1977, 
         'Diretor': 'George Lucas'}
print(filme.values())        
print(filme.keys())        
print(filme.items())
for k, v in filme.items():
    print(f'O {k} é {v}')'''

#pessoas = {'nome': 'Mafa', 'sexo': 'M', 'idade': 27}
# print(pessoas['nome'])
# print(pessoas['sexo'])
# print(pessoas['idade'])
#print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
# print(pessoas.keys())
# print(pessoas.values())
# print(pessoas.items())
#del pessoas['sexo']
#pessoas['nome'] = 'Leandro'
#pessoas['peso'] = 98.5
'''for k in pessoas.keys():
    print(k)
for k in pessoas.values():
    print(k)
for k, v in pessoas.items():
    print(f'{k} = {v}')'''

'''brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0])
print(brasil[0]['uf'])
print(brasil[1]['sigla'])'''

'''estado = {}
brasil = []
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')
    for v in e.values():
        print(v, end=' ')
    print()'''