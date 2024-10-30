#G) Você está desenvolvendo um programa para determinar se três segmentos podem formar um triângulo. 
# Para isso, o programa precisa receber as medidas dos três segmentos e compará-las entre si. 
# A resposta resultante dessa comparação deve indicar se os segmentos fornecidos podem formar um triângulo ou não.

import os


os.system('cls')

print('='*70)
print('VAMOS DESCOBRI SE O TRIANGULO PODE EXISTIR')
print('='*70)
print()

a = int(input('Me diga o primeiro lado do triangulo: '))
b = int(input('Me diga o segundo lado do triangulo: '))
c = int(input('Me diga o terceiro lado do triangulo: '))

if (a < b + c) and (b < a + c) and (c < b + a):
    print(f"As medidas {a}, {b} e {c} podem formar um triangulo!")
else:
    print('Essas medidas não podem formar um triangulo!')

print()