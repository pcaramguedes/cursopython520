## context manager


with open('texto.txt','r') as arquivo:
    conteudo = arquivo.read()

conteudo += 'qualquer coisa\n'

with open('texto.txt','a') as arquivo:
    arquivo.write(conteudo)

print(conteudo)
