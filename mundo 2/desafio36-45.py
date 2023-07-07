import datetime
import random

#########################36#########################
'''valor = float(input('Digite o valor da casa em interesse: R$'))
salario = float(input('Qual o valor do seu salario? R$'))
anos = int(input('Em quantos anos deseja pagar a casa? '))
prestacao = valor / (anos * 12)
if prestacao > salario * 0.3:
    print('Infelizmente não será possível esse empréstimo')
else:
    print(f'Parabéns, empréstimo aprovado!\nO valor das prestações será de: R${prestacao :.2f}')'''
#########################37#########################
'''numero = int(input('Digite um número inteiro qualquer: '))
escolha = int(input('Agora escolha a base de conversão: \n-1 para binário\n-2 para octal\n-3 para hexadecimal\n'))
if escolha == 1:
    print(bin(numero)[2:])
elif escolha == 2:
    print(oct(numero)[2:])
elif escolha == 3:
    print(hex(numero)[2:])
else:
    print('Escolha nao permitida, tente outra vez.')'''
#########################38#########################
'''n1 = int(input('Digite o primeiro valor inteiro: '))
n2 = int(input('Digite o segundo valor inteiro: '))
if n1 > n2:
    print('O primeiro valor é maior.')
elif n2 > n1:
    print('O segundo valor é maior.')
else:
    print('Não existe valor maior, os dois são iguais.')'''
#########################39#########################
'''ano = int(input('Digite o ano em que você nasceu: '))
dif = datetime.date.today().year - ano
qtd = abs(dif - 18)
if dif < 18:
    print(f'Voce ainda nao tem idade para se alistar, faltam {qtd} anos.')
elif dif == 18:
    print('Voce está na idade certa para se alistar.')
else:
    print(f'Voce ja passou da idade de se alistar em {qtd} anos.')'''
#########################40#########################
'''n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
if media < 5.0:
    print(f'Aluno Reprovado! {media :.1f}')
elif media >= 5 and media <= 6.9:
    print(f'Aluno em Recuperação! {media :.1f}')
else:
    print(f'Aluno Aprovado! {media :.1f}')'''
#########################41#########################
'''idade = int(input('Em que ano você nasceu? '))
cat = datetime.date.today().year - idade
if cat <= 9:
    print('Mirim')
elif cat <= 14:
    print('Infantil')
elif cat <= 19:
    print('Junior')
elif cat == 20:
    print('Senior')
else:
    print('Master')'''
#########################42#########################
'''r1 = int(input('Digite valor da reta 1: '))
r2 = int(input('Digite valor da reta 2: '))
r3 = int(input('Digite valor da reta 3: '))
if abs(r2 - r3) < r1 < (r2 + r3) and abs(r1 - r3) < r2 < (r1 + r3) and abs(r1 - r2) < r3 < (r1 + r2):
    print('Pode se formar um triangulo')
    if r1 == r2 and r2 == r3:
        print('Triangulo Equilatero!')
    elif r1 == r2 and r2 != r3 or r1 == r3 and r3 != r2:
        print('Triangulo Isosceles!')
    else:
        print('Triangulo Escaleno!')
else:
    print('Nao é possivel formar um triangulo')'''
#########################43#########################
'''peso = float(input('Qual o seu peso em Kg? '))
altura = float(input('Qual sua altura em metros? '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print(f'Abaixo do peso! {imc :.1f}')
elif imc >= 18.5 and imc < 25:
    print(f'Peso ideal! {imc :.1f}')
elif imc >= 25 and imc < 30:
    print(f'Sobrepeso! {imc :.1f}')
elif imc >= 30 and imc < 40:
    print(f'Obesidade! {imc :.1f}')
else:
    print(f'Obesidade Morbida! {imc :.1f}')'''
#########################44#########################
'''preco = float(input('Digite o valor normal do produto: R$'))
modo = int(input('Qual o modo de pagamento?\n-1 A vista dinheiro/cheque\n-2 A vista no cartao\n-3 Em ate 2x no cartao\n-4 3x ou mais no cartao\n'))
if modo == 1:
    valor = preco - preco * 0.1
    print(f'O valor será de: R${valor :.2f}')
elif modo == 2:
    valor = preco - preco * 0.05
    print(f'O valor será de: R${valor :.2f}')
elif modo == 3:
    print(f'O valor será de: R${preco :.2f}')
elif modo == 4:
    valor = preco + preco * 0.2
    print(f'O valor será de: R${valor :.2f}')
else:
    print('Opçao incorreta, por favor tentar novamente!')'''
#########################45#########################
'''escolha = str(input('Escolha entre Pedra, papel ou tesoura: ')).strip()
opc = ['PEDRA', 'PAPEL', 'TESOURA']
escolha = escolha.upper()
pc = random.choice(opc)
if escolha == 'PEDRA' and pc == 'PAPEL':
    print(f'O PC ganhou!! {pc} vence {escolha}')
elif escolha == 'PEDRA' and pc == 'TESOURA':
    print(f'Voce ganhou!!! {escolha} vence {pc}')
elif escolha == 'PAPEL' and pc == 'PEDRA':
    print(f'Voce ganhou!!! {escolha} vence {pc}')
elif escolha == 'PAPEL' and pc == 'TESOURA':
    print(f'O PC ganhou!! {pc} vence {escolha}')
elif escolha == 'TESOURA' and pc == 'PEDRA':
    print(f'O PC ganhou!! {pc} vence {escolha}')
elif escolha == 'TESOURA' and pc == 'PAPEL':
    print(f'Voce ganhou!!! {escolha} vence {pc}')
elif escolha == pc:
    print(f'Foi empate!!! {escolha} e {pc}')
else:
    print('Escolha invalida')''' 