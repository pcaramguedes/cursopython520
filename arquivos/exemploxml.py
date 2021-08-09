#from defusedxml import ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, ElementTree, Comment

# Raiz do XML

raiz = Element('partida')
raiz.append(Comment('Partida realizada em 2002 com o gol antologico'))


# Adicionar os elementos à arvore

ano = SubElement(raiz,'ano')
ano.text = '2002'

torneio = SubElement(raiz,'torneio')
torneio.text = 'Rio Sao Paulo'

times = SubElement(raiz,'times')
mandante = SubElement(times, 'mandante')
mandante.text = 'Sao Paulo'
visitante = SubElement(times, 'visitande')
visitante.text = 'Palmeiras'
resultado = SubElement(raiz, 'resultado')
resultado.text = '4x2'
gols = SubElement(raiz,'gols')
mandante1 = SubElement(gols, 'mandante')
jogador1 = SubElement(mandante1, 'Jogador1')
jogador1.text = 'Franca'
jogador2 = SubElement(mandante1, 'Jogador2')
jogador2.text = 'Kaka'

ElementTree(raiz).write('saida.xml')


