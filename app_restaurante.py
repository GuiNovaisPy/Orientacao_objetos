from Modelos.restaurante import Restaurante




if __name__ == '__main__':
    
    restaurante_1 = Restaurante(nome='paris 6',categoria='Gourmet',ativo=False)
    restaurante_2 = Restaurante(nome='bar do ze',categoria='bar',ativo=True).receber_avaliacao(cliente="guilherme",nota=10)

    Restaurante.listar_restaurantes()