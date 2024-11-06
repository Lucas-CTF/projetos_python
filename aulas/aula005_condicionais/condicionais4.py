







import os

#essas duas linhas que eu saltei é devido ao jeito pythonico de codar, de acordo com a autopep8 que é tipo a abnt do python
os.system('cls')

#declaração
a = 10
b = 5
c = 'John'

print('-' *70)
print('Condicionais: Operadores Lógicos')
print('=' *70)

#E (and) VERDADEIRO
print('E (and) VERDADEIRO')
if (a > 5 and b != c):
    print('Verdadeiro: Bloco executado')
else:
    print('Falso: Bloco executado')
    
print('.' *70)

# E (and) FALSO
print('E (and) FALSO')
if (a> 5 and b == c):
    print('Verdadeiro: Bloco executado')
else:
    print('Falso: Bloco executado')
    
print('.'*70)

# OU (or) VERDADEIRO
print('OU (or) VERDADEIRO')
if (a > 5 or b == c):
    print('Verdadeiro: Bloco executado')
else:
    print('Falso: Bloco executado')
    
print('.' *70)

# OU (or) FALSO
print('OU (or) FALSO')
if (a < 5 or c == 'Jane'):
    print('Verdadeiro: Bloco executado')
else:
    print('Falso: Bloco executado')
print('.' *70)
print()