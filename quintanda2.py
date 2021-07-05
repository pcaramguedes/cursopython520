#!/usr/bin/python3
import time
import os
opcao = 0
dicionario = {}
somaBanana = 0
somaMelancia = 0
somaMorango = 0
total=0

while True:
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

    print('1: Ver cesta       ')
    print('2: Adicionar frutas')
    print('3: Checkout        ')
    print('4: Sair            ')

    opcao = input('\nDigite a opcao deseja: ')

    if opcao == '2':
        
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

            time.sleep(1.5)

            if os.name == 'nt':
                os.system('cls')
            else:
                os.system('clear')

    elif opcao == '1':
        for frutas, valor in dicionario.items():
            print(frutas,": ", valor)

        time.sleep(3)
    elif opcao == '3':
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
        total=0
        time.sleep(4)
    elif opcao == '4':
        break
    else:
        print('Opcao digitada invalida !!!')

 
