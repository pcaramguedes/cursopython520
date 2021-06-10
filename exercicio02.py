#!/usr/bin/python3

frase = input('Digite uma frase qualquer: ')
print('Frase digitada: ', frase)

caracter = input('Escolha um caracter qualquer da frase: ')

alterada = frase.replace(caracter, ' ')

print('Frase alterada: ', alterada)
