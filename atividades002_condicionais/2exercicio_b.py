#B) A empresa "DataMax" está desenvolvendo um novo software de análise estatística e precisa de uma funcionalidade que permita aos usuários inserir três números e, em seguida, 
# exibir na tela qual é o maior número, qual é o menor número ou se os números são todos iguais. Essa funcionalidade é crucial para os analistas de dados da "DataMax" 
# que trabalham com conjuntos de dados diversos e precisam rapidamente identificar as características básicas desses conjuntos, como a presença de outliers ou a uniformidade dos números.

import os

os.system('cls')

print('=' *70)
print('Verificação de maior e menor.')
print('='*70)
print()

num1 = int(input('Me diga o primeiro numero: '))
num2 = int(input('Me diga o segundo numero: '))
num3 = int(input('Me diga o terceiro numero: '))
print()

print('=' *70)
print('RESULTADOS')
print('='*70)
print()

#if para descobrir se são iguais
if num1 == num2 == num3:
    print(f"Os numeros {num1}, {num2} e {num3} são iguais!")
else:
    print()


#if para descobri o maior  
if num1 > num2 and num1 > num3:
    print(f'O numero {num1} é o maior numero')
elif num2 > num1 and num2 > num3:
    print(f'O numero {num2} é o maior numero')
elif num3 > num1 and num3 > num2:
    print(f'O numero {num3} é o maior numero')
else:
    print()
    

#if para descobri caso aja dois maiores
if num1 == num2 > num3:
    print(f'Os numero {num1} e {num2} são os maiores')
elif num1 == num3 > num2:
    print(f'Os numero {num1} e {num3} são os maiores')
elif num3 == num2 > num1:
    print(f'Os numero {num3} e {num2} são os maiores')
else:
    print()


#if para descobri o menor  
if num1 < num2 and num1 < num3:
    print(f'O numero {num1} é o menor numero')
elif num2 < num1 and num2 < num3:
    print(f'O numero {num2} é o menor numero')
elif num3 < num1 and num3 < num2:
    print(f'O numero {num3} é o menor numero')
else:
    print()
    

#if para descobri caso aja dois menores
if num1 == num2 < num3:
    print(f'Os numero {num1} e {num2} são os menores')
elif num1 == num3 < num2:
    print(f'Os numero {num1} e {num3} são os menores')
elif num3 == num2 < num1:
    print(f'Os numero {num3} e {num2} são os menores')
else:
    print()
    
print()