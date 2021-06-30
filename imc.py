#!/usr/bin/python3

peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print(f'Baixo peso:{imc:.2f}')
elif imc < 24.9:
    print(f'Peso normal: {imc:.2f}')
elif imc < 29.9:
    print(f'Pre obesidade: {imc:.2f}')
elif imc < 34.9:
    print(f'Obesidade Grau I: {imc:.2f}')
elif imc < 39.9:
    print(f'Obesidade Grau II: {imc:.2f}')
else:
    print(f'Obesidade Grau III: {imc:.2f}')
