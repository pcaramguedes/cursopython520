arquivo = open('texto.txt','r')
conteudo = arquivo.readlines()

arquivo.close()
arquivo = open('texto.txt','a')


arquivo.write('Adicionei uma nova linha de novo\n')

arquivo.close()

for num in range(0,len(conteudo)):
    print(f'{num}: {conteudo[num]}')
