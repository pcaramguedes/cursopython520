import os
from time import sleep

def limpa():
    if os.name == 'nt':
        os.system('cls')
    os.system('clear')
    
soma = lambda x,y: x+y
subtracao = lambda x,y: x-y
multiplicacao = lambda x,y: x*y

def divisao(x,y):
    if y != 0:
       return print(f'\n {x/y}')
    
    return print('\nDivisor nao pode ser 0')

def sair(*args):
    exit()

# Direcionar o fluxo da aplicacao
dicios = {
    '1':soma,
    '2':subtracao,
    '3':multiplicacao,
    '4':divisao,
    '5':sair
}
def menu(*msg):
    while True:
        limpa()
        n1 = float(input('Digite o N1: '))
        n2 = float(input('Digite p N2: '))
        print('\n')
        for op in msg:
            print(f'{op}')
            
        opcao=input('Escolha a opcao: ')

        if opcao in dicios.keys():
            print(dicios[opcao](n1,n2))
        else:
            print('\nOpcao inválida !!!')
        sleep(2)
if __name__ == '__main__':
    menu('1-Soma','2-Subtracao','3-Multiplicacao','4-Divisao','5-Sai')
    
    


