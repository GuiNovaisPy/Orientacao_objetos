class Musica:
    
    '''Objeto para a criação de musicas'''
    
    nome =  ''
    artista = ''
    duracao = ''




instance_rock = Musica()
instance_rock.nome = 'Metal'
instance_rock.artista = 'Guilherme'
instance_rock.duracao = '3min'

print(f'''Titulo: Rock
      
    Nome msc:'{instance_rock.nome}
    Artista: {instance_rock.artista}
    Duracao msc: {instance_rock.duracao}
''')   



instance_samba = Musica()
instance_samba.nome = 'Samba'
instance_samba.artista = 'Jorge'
instance_samba.duracao = '1min'

print(f'''Titulo: Samba
      
    Nome msc:{instance_samba.nome}
    Artista: {instance_samba.artista}
    Duracao msc: {instance_samba.duracao }
''')   