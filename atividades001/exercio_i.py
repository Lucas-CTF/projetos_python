#Desenvolva um programa que solicite um valor em reais e calcule quantos dólares podem ser comprados com esse valor.
#No momento o valor do dolar é de R$ 5,71, irei usar esse valor para conversão

import os

os.system('cls')

print('CONVERSÃO REAL PARA DOLAR')
print()

real = float(input('Me diga quantos reais você possui: '))
print()

dolar = real / 5.71

print(f'Você possui em real: R$ {real} \nConversão para dolar: $ {dolar} ')
print()