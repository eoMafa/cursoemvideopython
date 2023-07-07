import lib.interface
import lib.arquivo
import time

arq = 'E:\estudos\cursoemvideopython\mundo 3\desafio115\pessoasCadastradas.txt'

if not lib.arquivo.arqExiste(arq):
    lib.arquivo.criarArquivo(arq)
while True:
    resposta = lib.interface.menu(
        ['Ver Pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        lib.arquivo.lerArquivo(arq)
    elif resposta == 2:
        lib.interface.cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: ')).strip().lower().capitalize()
        idade = int(input('Idade: '))
        lib.arquivo.cadastrar(arq, nome, idade)
    elif resposta == 3:
        lib.interface.cabecalho('Saindo do sistema... Até Logo!')
        break
    else:
        print('\033[0;31mERRO! Digite uma opção válida!\033[m')
    time.sleep(2)
