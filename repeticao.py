#!/usr/bin/python3






exit()
texto = """               

o rato roeu a ropa do rei de roma

"""
vogal = 0

for caractere in texto:
    if caractere.lower() in 'aeiou':
        vogal += 1

print('Total de vogais: {}'.format(vogal))



exit() 
lista_de_compras = [
    ('Camiseta',19.90),
    ('Calca Jeans',20.50),
    ('Meia G', 5.90)

]

total=0
desconto=0.90

for chave in lista_de_compras:
    print(chave)
    if chave[0].upper() == 'CAMISETA':
        total +=chave[1] * desconto
    else:
        total += chave[1]

print(f'Soma: {total:.2f}')

