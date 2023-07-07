percorrido = float(input('Quantos km foram rodados nesse carro? '))
dias = int(input('Quantos dias que utilizaram o carro? '))
total = (percorrido * 0.15) + (dias * 60)
print(f'O total a pagar é de {total :.2f}')