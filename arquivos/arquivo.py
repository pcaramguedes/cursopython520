## Abertura  de arquivo no modo de gravacao

# Abertura em modo de escrita
## Primeiramente eh importante abrir o arquivo em modo leitura
## Ler o conteudo e fechar e depois abrir em modo de escrita


arquivo = open('texto.txt','r')


conteudo = arquivo.readlines()
arquivo.close()
conteudo.append('Nova linha de exemplo')

arquivo = open('texto.txt','w')

arquivo.writelines(conteudo)
arquivo.close()

print(conteudo)

