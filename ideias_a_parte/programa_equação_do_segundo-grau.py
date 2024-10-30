#importando biblioteca
import os

#usando comando da biblioteca para limpar o terminal
os.system('cls')

#TITULO
print('='*70)
print('VAMOS CALCULAR A UMA FUNÇÃO QUADRATICA E DESCOBRIR SUAS RAIZES')
print('='*70)
print()

#entrada
a = int(input('Me diga o valor de A: '))
b = int(input('Me diga o valor de B: '))
c = int(input('Me diga o valor de C: '))

reposta_do_usuario = str(input(f'A equação que você digitou é {a}x^2 {b} {c} = 0? '))
print()

if reposta_do_usuario == 'sim':
#PROCESSAMENTO
    delta = ((b**2) - 4 * a * c)
    raizdedelta = delta ** 0.5
    raiz1 = (-b - raizdedelta) / (2 * a)
    raiz2 = (-b + raizdedelta) / (2 * a)
#SAIDA
    print(f'Delta = {delta}')
    print(f'Raiz quadrada de delta = {raizdedelta}')
    print(f'As raizes da sua equação são: {raiz1} e {raiz2}')
else: 
    print('Renicie o programa!')