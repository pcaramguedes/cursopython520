class Colaborador:

    def __init__(self):
        self.nome = ''
        self.endereco = ''
        self.idade = 0
        self.salario = 0.0
        self.cargo = ''
        self.encargos = 0.25

    def apresentaColaborador(self):
        return f'Nome: {self.nome}' \
               f'Cargo: {self.cargo}' \
               f'Salario: {self.salario}'
class Gerente(Colaborador):
    pass
