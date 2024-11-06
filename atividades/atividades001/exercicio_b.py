#Crie um programa que pergunte o ano de nascimento do usuário e calcule sua idade atual.

import os
import datetime

os.system('cls')

anodn = int(input('Qual ano você nasceu? '))
anoa = datetime.datetime.now()
idade = anoa.year - anodn

print(f'Você tem {idade} anos!')
print()