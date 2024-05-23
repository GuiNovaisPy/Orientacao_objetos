

class Restaurante:
    
    def __init__(self,nome,categoria) -> None: 
        
        #O __init__ é um metodo contrutor que é chamado quando instanciamos o nosso objeto,neste caso os args que passamos para o init, são obrigatorios e devem ser passados ao instanciar o nosso objeto
        
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        
    def __str__(self) -> str:
        
        # o __str__ é um metodo especial que te permite alocar algo que voce tenha de atributo no seu objeto e queira devolver ele na variavel de instancia do objeto
        return self.nome
        

restaurante_1 = Restaurante(nome='Restaurante 1',categoria='Gourmet')
print(restaurante_1)# printa oq for devolvido no metodo especial __str__ e se ele não existe printa o objeto e o espaço da memoria onde ele esta alocado

restaurante_1.nome = "Pizzaria"
print(restaurante_1)


print(f'''
Nome restaurante: {restaurante_1.nome}
Categoria restaurate: {restaurante_1.categoria}
Ativo? {restaurante_1.ativo}
''')




