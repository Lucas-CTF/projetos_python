import os


os.system('cls')

print('='*70)
print('Conversor para segundos')
print('='*70)
print()

horas = int(input('Me diga as horas: '))
minutos = int(input('Me diga os minutos: '))
segundos = int(input('Me diga os segundos: '))
print()

total = (horas * 3600) + (minutos * 60) + segundos

print(f"As horas {horas}:{minutos}:{segundos}")
print(f'Possuem {total} segundos')
print()