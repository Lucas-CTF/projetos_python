import os


os.system('cls')

print('-'*50)
print('ESTRUTURA DE CONTROLE SOMATORIO')
print('='*70)

print()

soma = 0

for var_iteradora in range(0, 4):
    numero = int(input(f'DIgite o {var_iteradora + 1}° numero: '))

    #calculo
    soma += numero #mesma coisa: soma = soma + numero

print('-'*50)
print(f'A soma dos numeros é: {soma}')
print('-'*50)
print()