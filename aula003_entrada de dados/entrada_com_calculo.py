import os

os.system('cls')

#esse é um program para calcular a area de um circulo, então define minha constante PI como 3.14
PI = 3.14

nome = input('Ola, qual seu nome? ')
print()
print('Ola', nome, ", vamos começar a calcular a area de um circulo?")
print()
c = float(input('Me diga qual o comprimento da circunferencia:'))
print()
d = float(input(c / PI))
r = float(input(d / 2))
a = float(input(r^2 * PI))
print('A area do seu circulo é: ', a)