#!/usr/bin/python3

flag=1
soma=0.0

while (flag <= 4):
    nota = float(input("Digite a nota: "))
    flag += 1
    soma += nota

print(f"A media das notas eh: {soma/(flag-1)}:")



