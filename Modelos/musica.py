class Musica:
    
    
    musicas = []
    
    def __init__(self,nome,artista,duracao) -> None:
    
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
        
        Musica.musicas.append(self.nome)
        
        
    def __str__(self) -> str:
        return self.nome
    
    
    def listar_todas_musicas(self) -> None:
        
        for musica in Musica.musicas:
            print(musica)




instance_rock = Musica(nome='Metal',artista='Guilherme',duracao='3min')
instance_samba = Musica('Samba','Jorge','1min')


instance_samba.listar_todas_musicas()

