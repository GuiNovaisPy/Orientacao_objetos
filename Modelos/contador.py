class Contador:
  

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