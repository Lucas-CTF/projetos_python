import math
import os


os.system('cls')

print('-'*50)
print('Estudo da biblioteca matematica MATH')
print('='*50)
print()

#entrada de dados
numero_decimal = float(input('Entre com um numero decimal: '))

#processamento
arredondador_para_cima = math.ceil(numero_decimal)
arredondador_para_baixo = math.floor(numero_decimal)

#saida
print('='*50)
print(f'O numero {numero_decimal} arredondado para cima é:\
      {arredondador_para_cima}')
print(f'O numero {numero_decimal} arredondado para baixo é:\
      {arredondador_para_baixo}')
print('-'*50)