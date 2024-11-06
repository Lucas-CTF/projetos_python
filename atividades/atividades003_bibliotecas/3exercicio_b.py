#Faça um programa que receba 2 valores, faça a divisão entre eles. Se a divisão não for inteira, o programa deverá arredondar o resultado para cima e para baixo. 
#Faça a validação para divisão por 0.

import os
import math


os.system('cls')

print('='*70)
print('DIVISÃO')
print('='*70)
print()

dividendo = float(input('Me diga o dividendo: '))
divisor = float(input('Me diga o divisor: '))
print()



if divisor == 0:
    print('NÃO PODE DIVIDIR NADA POR ZERO!')
else:
    divisão = dividendo / divisor
    arrendondamento_para_cima = math.ceil(divisão)
    arrendondamento_para_baixo = math.floor(divisão)
    if divisão.is_integer():
        print(f'{dividendo}/{divisor} = {divisão:.0f}')
    else:
        print(f'A divisão de {dividendo}/{divisor} é aproximandamente {divisão:.2f}')
        print(f'Arrendondado para cima = {arrendondamento_para_cima}')
        print(f'Arrendondado para baixo = {arrendondamento_para_baixo}')
print()