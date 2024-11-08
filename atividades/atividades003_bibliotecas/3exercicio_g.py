#Faça um programa que peça os valores de a, b e c de uma equação do 2º grau.
#Calcule as raízes da equação do 2º grau seguindo a fórmula: Δ = b² - 4ac, x = (-b ± raiz(Δ)) / (2a).

import os
import math


os.system('cls')

print("="*70)
print('Calculo de Função do 2° grau')
print('='*70)
print()

a = float(input('Insira A: '))
b = float(input('Insira B: '))
c = float(input('Insira C: '))
print()

delta = b**2 -(4 * a * c)
raiz_delta = math.sqrt(delta)
x1 = (-b + raiz_delta) / (2*a)
x2 = (-b - raiz_delta) / (2*a)

print(f'EQUAÇÃO: +{a}x² +{b}x +{c}')
resposta = input('A equação acima está correta? (sim/não): ').lower()

if resposta == 'sim':
    if delta < 0:
        print('Não existe raiz para delta negativo ')
    elif delta >= 0:
        print(f'Delta = {delta}')
        print(f'Raiz de delta = {raiz_delta}')
        print(f'XI = {x1}')
        print(f'XII = {x2}')

else:
    print('Renicie o programa!')
print()