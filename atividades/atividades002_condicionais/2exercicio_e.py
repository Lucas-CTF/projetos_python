#E) A empresa "TravelCalc" está desenvolvendo um sistema de cálculo de preços de passagens de ônibus com base na distância da viagem. 
#Eles precisam de um programa que solicite ao usuário a distância a desejada e, em seguida, calcule o preço da passagem de acordo com as políticas da empresa. 
#Segundo essas políticas, viagens de até 200 km têm um custo de R$0,70 por km rodado, enquanto viagens acima dessa distância passam a custar R$0,40 por km rodado.

import os


os.system('cls')

print('='*70)
print('CALCULO DE DISTANCIA')
print('='*70)
print()

distancia = float(input('Insira a distancia da viagem: '))
preço = float

if distancia <= 200:
    preço = distancia * 0.70
else:
    preço = distancia * 0.40
    
print(f'O valor da viagem para {distancia}km, sera de R$ {preço:.2f}')
print()