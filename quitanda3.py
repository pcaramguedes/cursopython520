#!/usr/bin/python3
import time
import os

dicionario = {}

def limpa():
    if os.name == 'nt':
        os.system('cls')
    os.system('clear')
    

def cesta():
    for frutas, valor in dicionario.items():
        print(frutas,": ", valor)

    time.sleep(3)

def checkout():
    total=0
    for fruta, valor in dicionario.items():
        if fruta == 'Banana':
            print(fruta,' Qtd:', valor, ' Total: ', valor * 6.50)
            total += valor * 6.50
        elif fruta == 'Melancia':
            print(fruta, ' Qtd:', valor, ' Total: ', valor * 3.50)
            total += valor * 3.50
        else:
            print(fruta, ' Qtd:', valor, ' Total: ', valor * 9.99)
            total += valor * 9.99
                

    print(f'\nTotal a pagar na compra:  {total:.2f}')
    time.sleep(4)


def adiciona():
    somaBanana = 0
    somaMelancia = 0
    somaMorango = 0
    while True:
        print('\nMenu de frutas')
        print('1 - Banana/Valor: 6.50  ')
        print('2 - Melancia/Valor: 3.50')
        print('3 - Morango/Valor: 9.99 ')
        print('4 - Volta               ')
        fruta = input('Digite a fruta desejada: ')
        
        if fruta == '1':
            somaBanana += 1
            dicionario['Banana'] = somaBanana
        elif fruta == '2':
            somaMelancia += 1
            dicionario['Melancia'] = somaMelancia
        elif fruta == '3':
            somaMorango += 1
            dicionario['Morango'] = somaMorango
        elif fruta == '4':
            break
        else:
            print('Opcao invalida')

        if fruta in '123':
            print('Adicionado na cesta com Sucesso !!!')

        time.sleep(0.5)
        limpa()


dicOpcoes = {
    '1':cesta,
    '2':adiciona,
    '3':checkout,
    '4':lambda *args: exit()
}

def menu():

    while True:
        limpa()    
        print('1: Ver cesta       ')
        print('2: Adicionar frutas')
        print('3: Checkout        ')
        print('4: Sair            ')

        opcao = input('\nDigite a opcao deseja: ')
    
        if opcao in dicOpcoes.keys():
            dicOpcoes[opcao]()
        else:
            print('\nOpcao Inválida !!!')

if __name__ == '__main__':
    menu()
 