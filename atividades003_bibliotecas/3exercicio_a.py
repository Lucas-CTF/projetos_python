#Faça um programa que receba um valor e mostre sua raiz quadrada. Para raízes que não são exatas, arredonde para cima ou para baixo. 
#Faça a validação para números negativos, avisando ao usuário que o resultado será um número complexo.
#aqui iremos usar a biblioteca math

#importando as bibliotecas
import os
import math


os.system('cls')

print('='*70)
print('RAIZ QUADRADA')
print('='*70)
print()

num = float(input('Me diga o numero que iremos ver a raiz quadrada: '))
print()

if num < 0:
    print("Sera um numero complexo")
else:
    #função que usamos para calcular a raiz quadrada em vez de usar "raiz = num ** 0.5"
    raiz = math.sqrt(num)
    #função que usamos para arredondar
    arrendondamento_para_cima = math.ceil(raiz)
    arrendondamento_para_baixo = math.floor(raiz)
    #Aqui estou usando para verificar se o nuemro é inteiro, pois se for nã oprecisa arredondar
    if raiz.is_integer():
        print(f'A raiza quadrada de {num} é {raiz}.')
    else:
        print(f'A raiza quadrada de aproximadamente {num} é {raiz:.2f}.')
        print(f'Arrendondado para cima = {arrendondamento_para_cima}')
        print(f'Arrendondado para baixo = {arrendondamento_para_baixo}')

print()
