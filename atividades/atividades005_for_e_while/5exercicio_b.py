#Evolua o programa anterior para um código que pergunte ao usuário qual o intervalo que ele deseja ver  impresso.

import os


os.system('cls')

print('='*70)
print('Numeros')
print('='*70)
print()

incio = int(input('Me diga a partir de qual numero começara imprimir: '))
fim = int(input('Me diga onde parar de imprimir: ')) +1 #se pedir pra imprir ate o 10, ele vai só ate o 9, para resolver isso o "+1"

for var_iteradora in range (incio, fim):
    print(var_iteradora, end=' ')