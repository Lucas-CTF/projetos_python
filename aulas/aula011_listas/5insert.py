import os


os.system('cls')

#Lista original
lista = [1, 2, 3, 4,]

#Pedindo ao usuario para fornecer a
#posição e o elemento a ser inserido
posicao = int(input("Posição onde deseja inserir o elemento: "))
elemento = input("Elemento a ser inserido: ")

#Verificando se a posição fornecida pelo usuario é valida
if posicao >= 0 and posicao <= len(lista):
    #Inserindo o elemneto na lista posição especificada pelo usuario
    lista.insert(posicao, elemento)
    print("Lista após a inserção:", lista)
else:
    print(f"Posição fora do intervalo 0, {len(lista)}")