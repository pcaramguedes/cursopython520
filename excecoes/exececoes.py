dic = {
    '1': lambda x,y: x + y,
    '2': lambda x,y: x - y,
    '3': lambda x,y: x * y,
    '4': lambda x,y: x / y,
    '5': lambda x,y: exit()

}

while True:

    try: # bloco com potencial travamento
        n1 = float(input('Digite N1: '))
        n2 = float(input('Digite N2: '))

        op = input(f'Digite a opção desejada \n' \
                f'1 - Soma \n' \
                f'2 - Subtração \n' \
                f'3 - Multiplicação \n' \
                f'4 - Divisão \n' \
                f'5 - Sair \n')

        res = dic[op](n1,n2)
    except ZeroDivisionError:
        print('Nao dividiras por zero')
    except KeyError:
        print('Digite uma opcao válida ')
    except ValueError:
        print('Digite apenas numeros')
    except Exception as err:
        print('Erro desconhecido', err)
    else:
        # proxima instrucao caso for bem sucedido
        print(res)
    finally:
        print('Passei por aqui')
        

