import pygame
import sys
from typing import Tuple, List
import load_obstacles


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (245, 230, 66)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

class GridModel:
    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col
        self.grid = [[0] * col for _ in range(row)]

    def set_cell(self, row: int, col: int, value: int):
        if 0 <= row < self.row and 0 <= col < self.col:
            self.grid[row][col] = value

    def get_cell_value(self, row: int, col: int) -> int:
        return self.grid[row][col]

class GridView:
    def __init__(self, row: int, col: int, width: int, height: int, margin: int):
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.margin = margin
        self.states = []

    def draw_grid(self, window, model):
        for row in range(self.row):
            for col in range(self.col):
                self.grid[row].append(0) 
        
        # inicialização
        pygame.init()
        # display e tamanho da interface
        janela = pygame.display.set_mode(((self.col*self.height) + self.col + 1, (self.row*self.width) + self.row+1))
        # named window
        pygame.display.set_caption("Path Planning")  
        
        obs = load_obstacles().load('environment/maps/map.txt')
        
        for ob1, ob2 in obs:
            if 0 <= ob1 < len(self.grid) and 0 <= ob2 < len(self.grid[0]):
                self.grid[ob1][ob2] = 4
        
        for row, col in self.states:
            # verifica se linha e coluna estão no limite da grade
            if 0 <= row < len(self.grid) and 0 <= col < len(self.grid[0]):
                self.grid[row][col] = 1 
            if (row, col) == (self.states[0]):
                self.grid[row][col] = 2 
            if (row, col) == (self.states[-1]):
                self.grid[row][col] = 3
            print("Coordinates: ", row, col)
            
            
        FPS = 30
        timer = pygame.time.Clock()
        done = True        
        while done:
            # eventos
            for evento in pygame.event.get(): 
                # se o evento foi um pedido para sair
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
       
                elif evento.type == 768:
                    done = False
                                    
            # pinta a janela de BLACK
            janela.fill(BLACK)
            # desenha o grid na janela
            for row in range(self.row):
                for col in range(self.col):
                    cor = WHITE

                    if self.grid[row][col] == 1:
                        cor = YELLOW
                    elif self.grid[row][col] == 2:
                        cor = RED
                    elif self.grid[row][col] == 3:
                        cor = GREEN
                    elif self.grid[row][col] == 4:
                        cor = BLACK
                
                    # desenha o grid e pinta se receber o evento
                    pygame.draw.rect(janela, cor, [(self.margin + self.width) * col + self.margin,
                    (self.margin + self.height) * row + self.margin, self.width, self.height])
                    
                    
            # dispara o timer
            timer.tick(FPS)
            # atualiza a janela
            pygame.display.flip()

if __name__ == "__main__":
    # Example usage
    states = [(1, 2), (3, 4)]  # Example states
    app = PathPlanningApp(10, 10, 30, 30, 1, states)
    app.run()
