from time import sleep
from os import system,name
from bibliotecas.calculadora import *

def limpa():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

def sair(*args):
    exit()

dicios = {
    '1':soma,
    '2':subtrair,
    '3':divisao,
    '4':multiplicar,
    '5':sair
}

def main(*op):
    while True:
        limpa() 
        
        n1 = float(input('Digite o Num 1: '))
        n2 = float(input('Digite o Num 2: '))

        for msg in op:
            print(f'{msg}')

        opcao = input('\nEscolha a opcao: ')

        if opcao in dicios.keys():
            print(dicios[opcao](n1,n2))
        else:
            print('\nOpcao invalida !!')

        sleep(3)




if __name__ == '__main__':
    main('1-Soma','2-Subtrair','3-Divisao','4-Multiplicar','5-Sair')


