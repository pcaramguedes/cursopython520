#!/usr/bin/python3


# Tuplas listas

matriz = [
    [ 0, 1, 2 ],
    [ 3, 4, 5 ],
    [ 6, 7, 8 ]
]

soma = 0

for lin in range(len(matriz)):
    print(matriz[lin])

    for col in range(len(matriz[lin])):
        print(matriz[lin][col])

        soma += matriz[lin][col]

print(f"A soma dos numeros da matriz eh: {soma}")

