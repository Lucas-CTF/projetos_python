#Crie um programa que converta uma medida em metros para centímetros e milímetros.

#Vou fazer melhor, vou mandar converter em todas as medidas

import os

os.system('cls')

m = float(input('Me diga a medida em metros que irei fazer as converões dela: '))

km = m / 1000
hm = m / 100 
dam = m / 10

dm = m * 10
cm = m * 100
mm = m * 1000

print('='*70)
print('CONVERSÕES')
print('='*70)
print()

print(f'Kilometros: {km}km')
print(f'Hectometro: {hm}hm')
print(f'Decâmetro: {dam}dam')
print(f'Metros: {m}m')
print(f'Decimetro: {dm}dm')
print(f'Centimetro: {cm}cm')
print(f'Milimetro: {mm}mm')
print()