#Desenvolva um programa que solicite três valores ao usuário. Em seguida, calcule e exiba a soma e a multiplicação desses valores.

import os
 
os.system('cls')

print('='*70)
print("Vamos calcular a soma de multiplição de três valores inteiros!")
print('='*70)
print()

print('='*70)
n1 = int(input('Insira o primeiro numero: '))
n2 = int(input('Insira o segundo numero: '))
n3 = int(input('Insira o terceiro numero: '))
print('='*70)
print()

soma = n1 + n2 + n3
mult = n1 * n2 * n3

print('='*70)
print('Resultados')
print('='*70)
print()
print(f'A soma de {n1} + {n2} + {n3} é = {soma}')
print(f'A multiplicação de {n1} x {n2} x {n3} é = {mult}')
print()