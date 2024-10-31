import os


os.system('cls')

print('='*70)
print('='*27, 'VAMOS CALCULAR', '='*27,)
print('='*70)
print()

num1 = float(input('Me diga o primeiro numero: '))
operação = input('Selecione o operador ( + , - , x , /): ')
num2 = float(input('Me diga o segundo numero: '))
print()

if operação == '+' :
    resposta = num1 + num2
elif operação == '-':
    resposta = num1 - num2
elif operação == 'x':
    resposta = num1 * num2
elif operação == '/':
    if num2 == 0:
        resposta = None
    else:
        resposta = num1 / num2
else:
    resposta = None
    
print()

print('='*70)
print('='*30, 'RESULTADO', '='*29,)
print('='*70)
print()

if resposta is not None:
    print(f'Operação: {num1} {operação} {num2} = {resposta}')
    print()
else:
    print("Resultado não disponível devido a erro na operação.")

print()
    