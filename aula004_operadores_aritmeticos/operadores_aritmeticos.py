import os

os.system('cls')

print('='*70)
print('Operadores Ariméticos')
print('='*70)
print()

#agora vamos entrar com os dados e irei comentar as operações
print('=== SOMA')
parcela1 = float(input('Entre com a 1° parcela: '))
parcela2 = float(input('Entre com a 2° parcela: '))
print()

print('=== SUBTRAÇÃO')
#minuendo é o que vai perder valor
minuendo = float(input('Entre com o minuendo: '))
#subtraendo é quem vai tirar valor do minuendo
subtraendo = float(input('Entre com o subtraendo: '))
print()

print('=== MULTIPLICAÇÃO')
#multiplicando é quem vai ser multiplicado
multiplicando = float(input('Entre com o multiplicando: '))
#aqui é alto explicação
multiplicador = float(input('Entre com o multiplicador: '))
print()

print('=== DIVISÃO')
#divindendo é quem vai ser dividido
dividendo = float(input('Entre com o dividendo: '))
#alto explicativo
divisor = float(input('Entre com o divisor: '))
print()

#AGORA VAMOS PROCESSAR ESSES DADOS
# o '+' é o operador de soma
soma = parcela1 + parcela2
# o '-' é o oeperador de subtração
subtração = minuendo - subtraendo
# o '/' é o operador de divisão
divisão = dividendo / divisor
# o '*' é o operador de multiplicação
multiplicação = multiplicando * multiplicador

#agora vamos dar saida nesses dados
print('='*70)
print('SEUS RESULTADOS:')
print('='*70)
print()

print(f'SOMA: {parcela1} + {parcela2} = {soma}')
print(f'SUBTRAÇÃO: {minuendo} - {subtraendo} = {subtração}')
print(f'MULTIPLICAÇÃO: {multiplicando} x {multiplicador} = {multiplicação}')
print(f'DIVISÃO: {dividendo} / {divisor} = {divisão}')
print('='*70)

