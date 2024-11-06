import os

os.system('cls')

#iremos trabalhar com operadores mais diferentes como potencia(**), resto(%), divisão inteira(//), raiz quadrada(**1/2(essa é a forma mais facil na minha visao)), raiz cubica(**1/3)
print('='*70)
print('VAMOS TRABALHAR COM POTENCIAÇÃO, DIVISÃO INTEIRA E RESTO')
print('='*70)
print()

n1 = float(input('Me diga o numero 1: '))
n2 = float(input('Me diga o numero 2: '))
print()

#aqui vamos  fazer as operações
pot = n1 ** n2
di = n1 // n2
ret = n1 % n2
#coloca os parenteses aqui porque sem eles o python entende de maneira errada
rq1 = n1 ** (1/2)
rq2 = n2 ** (1/2)
rc1 = n1 ** (1/3)
rc2 = n2 ** (1/3)

print('='*70)
print('RESULTADOS')
print('='*70)
print()
print(f'Potenciação de {n1} por {n2} é {pot}')
print(f'Divisão inteira de {n1} por {n2} é {di}')
print(f'Resto de {n1} por {n2} é {ret}')
print(f'Raiz quadrada de {n1} = {rq1}, enquanto de {n2} = {rq2}')
print(f'Raiz cubica de {n1} = {rc1}, enquanto de {n2} = {rc2}')
print('='*70)
print()