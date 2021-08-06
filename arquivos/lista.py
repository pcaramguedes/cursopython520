import random
from time import sleep

lista = [('12345','Paulo'),
         ('54321','Maria'),
         ('22222','Joao'),
         ('33333','Pedro')
]

while len(lista) > 1:
    print('Musica tocando...')
    sleep(1)    
    print('Musica Parou..')
    sleep(1)
    print('Participantes tentam sentar...')
    sleep(3)
    random.shuffle(lista)
    print(f'O Jogador  {lista.pop()[1]} saiu do jogo!')

print(f'O {lista[0][1]} Ganhou o jogo')
