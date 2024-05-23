
class Restaurante:
    
    restaurantes = []
    
    def __init__(self,nome,categoria) -> None: 
        
        #O __init__ é um metodo contrutor que é chamado quando instanciamos o nosso objeto,neste caso os args que passamos para o init, são obrigatorios e devem ser passados ao instanciar o nosso objeto
        
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self.nome)
        
    def __str__(self) -> str:
        
        # o __str__ é um metodo especial que te permite alocar algo que voce tenha de atributo no seu objeto e queira devolver ele na variavel de instancia do objeto
        return self.nome
    
    
    def listar_restaurantes(self) -> None:
        for item in Restaurante.restaurantes:
            print(item)

restaurante_1 = Restaurante(nome='Restaurante 1',categoria='Gourmet')
restaurante_2 = Restaurante(nome='Restaurante 2',categoria='bar')

restaurante_1.listar_restaurantes()

