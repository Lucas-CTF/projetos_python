import os

os.system('cls')

print('-'*70)
print("MEDIA DAS NOTAS")
print('-'*70)
print()

n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
n3 = float(input('Nota 3: '))
n4 = float(input('Nota 4: '))
print()

#aqui se não colocar entre parenteses da ruim por causa da ordem de precedencia
media_errada = n1 + n2 + n3 + n4 / 4
media_correta = (n1 + n2 + n3 + n4) / 4

print('-'*70)
print("RESULTADOS")
print('-'*70)
print()

print(f'Nota 1: {n1}   Nota 2: {n2}   Nota 3: {n3}   Nota 4: {n4}')
print()
print(f'Media errada: {media_errada}')
print(f'Media correta: {media_correta}')
print()
print('-'*70)
print()