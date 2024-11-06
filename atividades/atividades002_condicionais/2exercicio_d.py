#D) A empresa "SalaryBoost" está implementando um sistema automatizado para calcular os aumentos salariais de seus funcionários com base em critérios específicos. 
# Eles precisam de um programa que receba como entrada o salário atual de um funcionário e, em seguida, calcule o novo salário com base em determinadas condições. 
# Essas condições incluem um aumento de 5% caso o salário atual seja superior a R$1500,00, e um aumento de 10% caso o salário atual seja inferior a R$1000,00. 
# Além disso, o programa deve garantir que o salário informado não seja igual a zero ou negativo, pois isso não seria válido.

import os


os.system('cls')

print('='*70)
print('CALCULO DO SALÁRIO')
print('='*70)
print()

salario = float(input("Insira seu salário para calcular o aumento: "))
print()

novo = ''
resposta = ''

#aqui não encontrei um sinal para calculo de porcentagem, então fazemos desse jeito abaixo e usamos os parenteses por causa da ordem de precedencia
if salario <= 0:
    resposta = 'SALARIO INVALIDO!'
elif salario >= 1500.00:
    novo = salario * 1.05
    resposta = f'Seu antigo salario: R$ {salario:.2f}\nSeu novo salario: R$ {novo:.2f}'
elif salario <= 1000.00:
    novo = salario * 1.1
    resposta = f'Seu antigo salario: R$ {salario:.2f}\nSeu novo salario: R$ {novo:.2f}'
else:
    print('Seu salario se mantera o mesmo!')
    
print(resposta)
print()