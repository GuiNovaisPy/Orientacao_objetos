from Modelos.Cardapio.item_cardapio import ItemCardapio

class Bebida(ItemCardapio):#ou seja class Prato herda os atributos e metodos da class ItemCardapio
    
    def __init__(self,nome,preco,tamanho) -> None:
        super().__init__(nome,preco)
        self._tamanho = tamanho