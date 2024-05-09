from environment import create_grid

def main():
    ''' 
    Botão direito do mouse: insere o obstáculo
    Botão esquerdo do mouse: insere o gol
    Até o momento é salvo apenas o txt do obstáculo
    '''
    grid_instance = create_grid(8,8,50,50)
    grid_instance.main()
    grid_instance.save('environment/maps/map.txt')
        
if __name__== "__main__":
    main()