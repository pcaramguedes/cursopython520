#Clientes -> produtos -> carrinho {
#        adicionar item, remover item}

class Produto:

    def __init__(self, sku='',nome='',desc='',preco=0.0):
        self.sku = sku
        self.nome = nome
        self.desc = desc
        self.preco = preco


class CarrinhoDeCompras:

    def __init__(self):
        self.carrinho = []
        self.total = 0
        self.quantidade_produtos =0

    def adicionarProduto(self, produto):
        self.carrinho.append(produto)
        self.quantidade_produtos += 1

    def removerProduto(self,nome_produto):

        for produto in self.carrinho:
            if produto.nome == nome_produto:
                self.carrinho.remove(produto)
                print(f'O produto: {produto.nome} foi removido !!')
                break
        else:
            print(f'Produto: {nome_produto} nao encontrado !!')


    

        
