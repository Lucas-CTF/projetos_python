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
#termino depois