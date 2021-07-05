# Estudo de funcoes


def soma(*numeros):
    total = 0

    for num in numeros:
        print(num,end=' ')
        total += num;

    return total


print('\n',soma(1,2,3,4,5,100,99,200))

