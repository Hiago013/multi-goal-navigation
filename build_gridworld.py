from environment import create_grid

def main():
    '''
    Botão esquerdo do mouse: insere/deleta o obstáculo
    Salva o txt dos obstáculos
    '''
    grid_instance = create_grid(5,5,50,50)
    grid_instance.main()
    grid_instance.save('environment/maps/map.txt')

if __name__== "__main__":
    main()