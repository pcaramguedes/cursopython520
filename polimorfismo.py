class Profissao:

    def __init__(self):
        self.classe = ''
        self.habilidade = ''

class Mago(Profissao):

    def atacar(self):
        return 'Ataque com magia'

class Soldado(Profissao):

    def atacar(self):
        return 'Ataque de espada'

class Arqueiro(Profissao):

    def atacar(self):
        return 'ataque a distancia com arco e flecha'

