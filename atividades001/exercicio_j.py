#Elabore um programa que peça as dimensões de um retângulo e calcule seu perímetro.

#Importando biblioteca para limpea do terminal
import os

#Este comando é para limpar o terminal
os.system('cls')

#Organizando o terminal
print('='*70)
print('VAMOS CALCULAR O PERIMETRO DO RETANGULO!')
print('='*70)

#Entrada de dados
#Estou usando Casting para converter o valor das variaveis em float e me permitir usar numeros reais, caso necessario
#O perimetro do retangulo se calcula com "Duas vezes a soma da base com a altura"
#Define minhas variaveis base e altura
base = float(input('Me diga a qual o valor da base: '))
altura = float(input('Me diga a qual o valor da altura: '))
print()

#Agora sera feito o processamento desses dados
#Usei os parenteses por causa da ordem de precedencia
perimetro = (base + altura) * 2

#Saida dos dados
print('='*70)
print('RESULTADO')
print('='*70)
#Farei a saida de forma formatada
print(f'O Retangulo com base = {base} e altura = {altura} \nPossui o perimetro de valor: {perimetro} ')
print()