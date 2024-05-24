
class Restaurante:
    
    restaurantes = [] #tambem é um atributo da class
    
    def __init__(self,nome,categoria,ativo) -> None: 
        
        #O __init__ é um metodo contrutor que é chamado quando instanciamos o nosso objeto,neste caso os args que passamos para o init, são obrigatorios e devem ser passados ao instanciar o nosso objeto
        
        self._nome = nome.title()
        self._categoria = categoria.title()
        self._ativo = ativo #_define um metodo privado ou seja o valor destes atributos nao podem ser mudados do lado de fora do objeto por mais que ele esteja instanciado
        Restaurante.restaurantes.append(self)
        
    def __str__(self) -> str:
        
        # o __str__ é um metodo especial que te permite alocar algo que voce tenha de atributo no seu objeto e queira devolver ele na variavel de instancia do objeto
        return self._nome
    
    
    def listar_restaurantes(self) -> None:
        for item in Restaurante.restaurantes:
            print(item._nome)
            print(item._categoria)
            print(item.ativo)
            print(60*"-")
            
            
    @property
    def ativo(self) -> str:
        
        #property é um Decoretor do python que modifica como o atributo vai ser lido e acessado e que tambem nos permite utilizar os metodos 
        #setter, e deletter  
        
        #sempre que o atributo for chamado ele passa por aqui para "tratamento"
          
        return 'Ativo' if self._ativo is True else 'Inativo'
    
    def outra_funcao(self):
        print(self.ativo)
    
  
    


restaurante_1 = Restaurante(nome='Restaurante 1',categoria='Gourmet',ativo=False)
restaurante_2 = Restaurante(nome='Restaurante 2',categoria='bar',ativo=True)

restaurante_1.listar_restaurantes()



