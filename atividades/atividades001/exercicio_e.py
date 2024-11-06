#Faça um programa que receba um número inteiro e exiba seu sucessor e antecessor.
# fazer isso é mais facil do que parece quando se olha de primera, basta fazer o numero -1 e depois +1 para ter o sucessor e antecessor
import os

os.system('cls')

n = int(input('ME DIGA O NUMERO DO QUAL DESEJA SABER O SUCESSOR E ANTECESSOR: '))
print()

a = n - 1
s = n + 1

print(f'Referente ao numero {n}, o seu sucessor é {s} e seu antecessor é {a}.')
print()