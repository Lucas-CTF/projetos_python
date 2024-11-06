#importando bibliotecas
import os
import math


#limpando terminal
os.system('cls')

print('-'*70)
print('Estudo da biblioteca matematica MATH')
print('='*70)
print()

#declarações
base = 2
expoente = 3
angulo = 30
radicando = 81
co = 5
ca = 10

#processamento
potencia = math.pow(base, expoente)
raizQuadrada = math.sqrt(radicando)
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
hipotenusa = math.hypot(co, ca)

#saida
print(f'{base} elevado a {expoente} é igual a: {potencia}')
print(f'A raiz quadrada de {radicando} é: {raizQuadrada}')
print(f'O seno de {angulo} é: {seno:.2f}')
print(f'O consseno de {angulo} é: {cosseno:.2f}')
print(f'A tangente de {angulo} é: {tangente:.2f}')
print(f'O valor da hipotenusa é {hipotenusa:.2f}')
print('-'*70)