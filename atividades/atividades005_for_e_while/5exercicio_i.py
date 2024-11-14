#Faça um algoritmo que imprima a frase "estou em looping" e, em seguida, solicite ao usuário digitar uma letra. Caso a letra seja o “f" finalize a aplicação. Do contrário, imprima novamente a mesma frase até que o caractere “f" seja digitado.

import os


os.system('cls')

print('='*70)
print('ENTRANDO EM LOOPING..')
print('='*70)


while (True):
    resposta = str(input('Em looping, digite "f" para parar: ')).lower

    if resposta != 'f':
        print('Vamos continuar em looping enquanto isso...')
    
    else:
        break
print("Acabou o looping")