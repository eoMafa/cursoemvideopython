nome = str(input('Qual o seu nome? ')).strip()
if nome.upper() == 'MAFA':
    print('Gataooo!!!')
elif nome.upper() == 'PEDRO' or nome.upper() == 'MARIA' or nome.upper() == 'PAULO':
    print('Seu nome é muito popular no Brasil!')
elif nome.upper() in 'ANA CLAUDIA JESSICA JULIANA':
    print('Belo nome feminino!')
else:
    print('Seu nome é bem normal.')
print(f'Tenha um bom dia, {nome.title()}!')