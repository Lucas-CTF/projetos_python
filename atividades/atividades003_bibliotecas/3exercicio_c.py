#Faça um programa que receba as informações de base e expoente. Calcule a potência.

import os
import math


os.system('cls')

print('='*70)
print('POTENCIA')
print('='*70)
print()

num1 = float(input('Me diga a base: '))
num2 = float(input('Me diga o expoente: '))
print()

potencia = math.pow(num1, num2)
print(f'{num1}^{num2} = {potencia}')
print()