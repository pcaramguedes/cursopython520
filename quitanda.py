#!/usr/bin/python3
import time
import os
opcao = 0
dicionario = {}
somaBanana = 0
somaMelancia = 0
somaMorango = 0


while (opcao != 3):
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

    print('1: Ver cesta       ')
    print('2: Adicionar frutas')
    print('3: Sair            ')

    opcao = int(input('\nDigite a opcao deseja: '))

    if opcao == 2:
        
        while True:

            print('\nMenu de frutas')
            print('1 - Banana    ')
            print('2 - Melancia  ')
            print('3 - Morango   ')

            fruta = int(input('Digite a fruta desejada: '))
        
            if (fruta <1 or fruta >3):
                print('Opcao invalida..')
                time.sleep(2)
                break

            if fruta == 1:
                somaBanana += 1
                dicionario['Banana'] = somaBanana
                print('Adicionado na cesta com Sucesso !!!')
                time.sleep(1.5)
                break
            if fruta == 2:
                somaMelancia += 1
                dicionario['Melancia'] = somaMelancia
                print('Adicionado na cesta com Sucesso !!!')
                time.sleep(1.5)
                break
            if fruta == 3:
                somaMorango += 1
                dicionario['Morango'] = somaMorango
                print('Adicionado na cesta com Sucesso !!!')
                time.sleep(1.5)
                break
            else:
                print('Opcao invalida')
                time.sleep(1.5)
                
    
    elif opcao == 1:
        for frutas, valor in dicionario.items():
            print(frutas,": ", valor)

        time.sleep(3)
    elif opcao == 3:
        break
    else:
        print('Opcao digitada invalida !!!')

 
