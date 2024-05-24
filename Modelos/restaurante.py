from Modelos.avaliacao import Avaliacao


class Restaurante:
    
    restaurantes = [] #É um atributo da class
    
    def __init__(self,nome,categoria,ativo) -> None: 
        """O __init__ é um metodo contrutor que é chamado quando instanciamos o nosso objeto,
        neste caso os args que passamos para o init, são obrigatorios e devem ser passados ao instanciar o nosso objeto.
        
        "_" define um metodo privado ou seja o valor destes atributos 
        nao DEVEM ser mudados.
        """
        
        self._nome = nome.title()
        self._categoria = categoria.title()
        self._ativo = ativo 
        self._avaliacoes = []
        
        Restaurante.restaurantes.append(self)
        
    def __str__(self) -> str:
        """o __str__ é um metodo especial que te permite alocar algo que voce
        tenha de atributo no seu objeto e queira devolver ele na variavel de instancia do objeto"""
        
        return self._ativo
    
    
    @classmethod
    def listar_restaurantes(cls) -> None:
        """@classmethod é um decoretor utilizado para especificar que o metodo é um metodo referenciado a classe,
        não ao objeto que esta classe constrói, ou seja é um metodo que pode ser chamado direto sem instancia a classe.
        
        assim por exemplo: Restaurante.listar_restaurantes()
        Obs: Sem instanciar o Objeto Restaurante
        
        
        cls: é a referencia da classe para conseguirmos acessar o que desejamos
        
        """
        
        for item in cls.restaurantes:
            print("Nome restaurante:",item._nome)
            print("Categoria:",item._categoria)
            print("Ativo:",item.ativo) # modificado com o @property
            #print(item._ativo) # o reservado dentro do objeto(original)
            print("Avalicao:",item.media_avaliacoes)
           
            
           
            
            print(60*"-")
            
            
    @property
    def ativo(self) -> str:
        """@property é um Decoretor do python que modifica como o atributo vai ser lido e acessado
        sempre que o atributo for ACESSADO. """
          
        return 'Ativo' if self._ativo is True else 'Inativo'
    
    def alternar_estado(self):
        """Funcao para alternar estado do restaurante.
        negar um valor como abaixo inverte o valor bool atual"""
        
        self._ativo = not self._ativo 
        
        
    def receber_avaliacao(self,cliente,nota):
        avaliacao = Avaliacao(cliente,nota)
        self._avaliacoes.append(avaliacao)
        
    
    @property  
    def media_avaliacoes(self):
        if not self._avaliacoes:
            return 0
        
        soma_notas = sum(avaliacao._nota for avaliacao in self._avaliacoes)
        qtd_notas = len(self._avaliacoes)
        media_notas = round(soma_notas/ qtd_notas,1)
        return media_notas
    

    



