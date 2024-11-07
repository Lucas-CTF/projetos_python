#Faça um programa que receba uma frase e, em seguida, mostre quantas vezes as 
# vogais foram utilizadas.

import os


os.system('cls')

frase = input('Me diga a frase que usaremos: ')

quantiaA = frase.count('a')
quantiaE = frase.count('e')
quantiaI = frase.count('i')
quantiaO = frase.count('o')
quantiaU = frase.count('u')

quantidade = quantiaA+quantiaE+quantiaI+quantiaO+quantiaU

print
print(f"A letra 'A' aperarece {quantiaA} vezes")
print(f"A letra 'E' aperarece {quantiaE} vezes")
print(f"A letra 'I' aperarece {quantiaI} vezes")
print(f"A letra 'O' aperarece {quantiaO} vezes")
print(f"A letra 'U' aperarece {quantiaU} vezes")
print(f'As vogais aparecem: {quantidade}')