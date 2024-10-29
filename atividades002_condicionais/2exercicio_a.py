# A) A empresa "TechSolutions" contratou você para desenvolver um programa em Python que irá automatizar uma parte do seu sistema de processamento de dados. 
# Eles precisam de um programa que solicite ao usuário a entrada de um número inteiro e, em seguida, verifique se esse número é par ou ímpar. 
# Essa funcionalidade é essencial para o sistema deles, pois eles processam grandes conjuntos de dados e precisam classificar os números de forma eficiente para realizar cálculos específicos em cada tipo de número.

import os


os.system('cls')

print('=' *70)
print('Caracterização TechSolutions')
print('='*70)
print()

#lembre que (=) é 'recebe' e (==) é 'igual'
num = int(input('Digite um numero inteiro para verificar se é par ou impar: '))

if (num % 2 == 0):
    print(f'O numero {num} é par!')
else:
    print(f'O numero {num} é impar!')
print()