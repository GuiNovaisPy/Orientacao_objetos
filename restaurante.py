

class Restaurante:
    
    def __init__(self,nome,categoria) -> None: 
        
        #O init é um metodo contrutor que é chamado quando instanciamos o nosso objeto,neste caso os args que passamos para o init, são obrigatorios e devem ser passados ao instanciar o nosso objeto
        
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        

restaurante_1 = Restaurante(nome='Restaurante 1',categoria='Gourmet')
print(f'''
Nome restaurante: {restaurante_1.nome}
Categoria restaurate: {restaurante_1.categoria}
Ativo? {restaurante_1.ativo}
''')




