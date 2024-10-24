# BOM A PRINCIPIO O CODIGO TODO ESTA FEITO PERFEITAMENTE, POREM NÃO QUER IMPORTAR A BIBLIOTECA "SYMPY" OQUE FAZ DAR ERRO, CONSERTAREI QUANDO TIVER RESPOSTAS
import os
import math #essa biblioteca serve par importar uma função de raiz quadrada
import sympy #essa serve para importar uma de raiz cubica que a math não possui

os.system('cls')

print('='*70)
print('VAMOS CALCULAR RAIZ QUADRADA E RAIZ CUBICA')
print('='*70)
print()

n1 = float(input('Me diga o primeiro numero: '))
n2 = float(input('Me diga o segundo numero: '))
print()

#agora vamos usar as funções
#essa função é a de raiz quadrada que peguei da primeira biblioteca
rq1 = math.pow(n1)
rq2 = math.pow(n2)
#essa agora é a de raiz cubica que eu peguei da segunda biblioteca
rc1 = cbrt(n1)
rc2 = cbrt(n2)

print('='*70)
print('RESULTADOS')
print('='*70)
print()

print(f'A raiz quadrada de {n1} é {rq1}, enquanto a de {n2} é {rq2}')
print(f'A raiz cubica de {n1} é {rc1}, enquanto a de {n2} é {rc2}')
print('='*70)
print()