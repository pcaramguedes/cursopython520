# Estudo de funcoes
# Funcoes anonimas



def mensagem(msg=""):
    print(f'\n{msg}')

mensagem()

def soma(*numeros):
    total = 0
    print(type(numeros))
    for num in numeros:
        print(num,end=' ')
        total += num;

    return total


print('\n',soma(1,2,3,4,5,100,99,200))

# Dados Mutaveis

list = [1,2,3,"Paulo"]

for num in list:
    print(num, end=' ')
    
def incrementa_item(lists, item):
    lists.append(item)
    for l in lists:
        print(l, end=' ')

incrementa_item(list,'Joao')
incrementa_item(list,'Pedro')
