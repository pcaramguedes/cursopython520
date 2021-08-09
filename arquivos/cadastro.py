from time import sleep
from os import system, name

## |Arquivos em formato TXT/CSV
    
        
# Cadastro com readlines eh uma lista
# o primeiro elemento é um cabeçalho
# 

# Código,CNPJ,Nome,Fantasia,Endereco,Bairro,CEP,Cidade,UF,e-mail
#Código,CNPJ,Nome,Fantasia,Endereco,Numero,Complemento,Bairro,CEP,Cidade,UF,e-mail


flag = True
codigo = '0'

while True:
    system('clear')

    with open('clientes1.csv','r') as arquivo:
        conteudo = arquivo.readlines()
    
    cnpj = input('Digite o CNPJ: ')

    for indice in conteudo:
        codigo = indice.split(',')[0]
        if cnpj.upper() in indice.split(','):
            print('CNPJ: ',cnpj,'Cliente: ',indice.split(",")[3])
            print('Já cadastrado !!')
            sleep(2)
            flag = False
            break
    
    if flag == True:
        cod = str((int(codigo)+1))
        print(f'\nCNPJ: {cnpj} digitado nao encontrado !!')
        nome = input('NOME: ')
        fantasia = input('FANTASIA: ')
        endereco = input('END: ')
        num = input('NUMERO: ')
        complemento = input('COMPLEMENTO: ')
        bairro = input('BAIRRO: ')
        cep = input('CEP: ')
        cidade = input('CIDADE: ')
        uf = input('UF: ')
        email = input('E-MAIL: ')

        registro = f'{cod},{cnpj},{nome},{fantasia},{endereco},{num},{complemento},{bairro},{cep},{cidade},{uf},{email}\n'
        with open('clientes1.csv','a') as arquivo:
            arquivo.writelines(registro)

        print("Gravado !!!")
        sleep(1)

exit()
filtro_uf = input('Digite a UF: ')

for registro in conteudo:
    
    if filtro_uf.upper() in registro.split(','):
        print(f'COD: {registro.split(",")[0]}')
        print(f'CNPJ: {registro.split(",")[1]}')
        print(f'NOME: {registro.split(",")[2]}')
        print(f'FANTASIA: {registro.split(",")[3]}')
        print(f'END: {registro.split(",")[4]}')
        print(f'NUMERO: {registro.split(",")[5]}')
        print(f'COMPLEMENTO: {registro.split(",")[6]}')
        print(f'BAIRRO: {registro.split(",")[7]}')
        print(f'CEP: {registro.split(",")[8]}')
        print(f'CIDADE: {registro.split(",")[9]}')
        print(f'UF: {registro.split(",")[10]}')
        print(f'E-MAIL: {registro.split(",")[11]}')

