class Contador:
    '''
    Classe que representa um contador.
    A instância mantém um contador específico, enquanto um contador global é compartilhado por todas as instâncias.
    '''

    contador_global = 0

    def __init__(self):
        pass

    @classmethod
    def __str__(cls):
        return f'Contador: {cls.contador_global}'

    @classmethod
    def incrementar(cls):
        cls.contador_global += 1

    @classmethod
    def zerar_contador_global(cls):
        cls.contador_global = 0
        return 'Contador global foi zerado.'
 
 
i =  Contador()  
i.incrementar()
i.incrementar()
i.zerar_contador_global()
    
print(i.contador_global)