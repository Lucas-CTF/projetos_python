#Faça um programa que imprima os valores no intervalo definidos pelo usuário.  Defina 3 números que deverão ser ignorados, ou seja, que não serão impressos na tela.
import os


os.system('cls')

print('='*70)
print('IMPRIMINDO VALORES')
print('='*70)
print()

inicio = int(input('Me diga onde começamos: '))
fim = int(input('Me diga onde terminamos: ')) +1
print()

num0 = int(input('Me diga um numero a ser ignorado: '))
num1 = int(input('Me diga um numero a ser ignorado: '))
num2 = int(input('Me diga um numero a ser ignorado: '))

for var_iteradora in range (inicio, fim):
    if var_iteradora == num1:
        continue
    elif var_iteradora == num0:
        continue
    elif var_iteradora == num2:
        continue
    else:
        print(var_iteradora, end=' ')
print()