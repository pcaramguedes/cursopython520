# Algumas premissas. A capacidade total do ônibus é de 45 pessoas
# Nao poderá ter superlotação, quando o onibus ficar vazio nao poderá efetuar desembarque


class Onibus:
    
    def __init__(self,capacidade_total=45,capacidade_atual=0,velocidade=0.0,
                placa='',modelo=''):
        self.capacidade_total = capacidade_total
        self.capacidade_atual = capacidade_atual
        self.velocidade = velocidade
        self.placa = placa
        self.modelo = modelo

    def acelerar(self, velocidade):
        try:
            self.velocidade += velocidade
        except Exception as err:
            print('Mensagem do erro: ', err)
        else:
            return f'Velocidade atual {self.velocidade}'

    def frear(self):
        if self.velocidade == 0:
            return 'Onibus parado '
        self.velocidade = 0
        return f'Velocidade do ônibus: {self.velocidade} '


    def embarcar(self, qtd_passageiros):
        
        if self.capacidade_atual == self.capacidade_total:
            return f'Proibido embarcar os {qtd_passageiros} no Onibus, LOTADO'
        else:
            soma = self.capacidade_atual + qtd_passageiros
            if soma <= self.capacidade_total:
                self.capacidade_atual += qtd_passageiros
                return f'Embarcados :{qtd_passageiros} - Atual dentro Ônibus: {self.capacidade_atual}'

            else:
                return f'A qtd {qtd_passageiros} de passageiros para embarcar ultrapassa os limites permitidos'


    def desembarcar(self):
        if self.velocidade == 0:
        
        else:
            


