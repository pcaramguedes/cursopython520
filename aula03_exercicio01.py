import os
# Rotina de funcoes


def saudacao(param1):

    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

    print(f'\nOlá {param1}! Tudo bem com você')

texto = input('Digite o seu nome: ')

saudacao(texto)

