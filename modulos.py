def saudacao(msg):
    return print(msg)

def soma(*args):
    soma = 0
    for num in args:
        soma += num
    return soma

PI = 3.14


if __name__ == '__main__':
    saudacao('Ola mundao')

