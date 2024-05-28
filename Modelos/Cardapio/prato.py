from Modelos.Cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio):#ou seja class Prato herda os atributos e metodos da class ItemCardapio
    
    def __init__(self,nome,preco,descricao) -> None:
        super().__init__(nome,preco)#super é um objeto especial do python que permite que a gnt acesse informações de outra classe neste caso da nossa classe item cardapio
        self._descricao = descricao