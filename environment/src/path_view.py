# CLASS GRID
import pygame, sys
import os
from typing import Tuple, List
from .load_obstacles import load_obstacles


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (245, 230, 66)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
class path_view():
    def __init__(self,
                 row:int,
                 col:int,
                 states:List[Tuple[int, int, int]],
                 width : int = 50,
                 height : int = 50,
                 margin = 1,
                 ):

        """
        This Python function initializes an object with specified row, column, width, height, margin and states
        attributes.
        """
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.margin = margin
        self.states = states
        self.grid = []


    def save(self, path : str = ''):
        """
        The `save` function writes the coordinates of cells with a value of 2 in a grid to a file
        specified by the `path` parameter.
        """
        with open(path, 'w') as f:
                        for i in range(len(self.grid)):
                            for j in range(len(self.grid[0])):
                                if self.grid[i][j] == 1 or self.grid[i][j] == 2 or self.grid[i][j] == 3:
                                    f.write(f'{i} {j}\n')
        pygame.quit()


    def run(self):
        """
        The main function initializes a grid, sets up a Pygame window for path planning, handles mouse
        events to update the grid, and continuously updates the display.
        """
        # matriz
        for row in range(self.row):
            self.grid.append([])
            for col in range(self.col):
                self.grid[row].append(0) 
        
        pygame.init()   
        janela = pygame.display.set_mode(((self.col*self.height) + self.col + 1, (self.row*self.width) + self.row+1))
        pygame.display.set_caption("Path Planning")  
        
        # obstacles
        obs = load_obstacles().load('environment/maps/map.txt')
        for row, col in obs:
            if 0 <= row < len(self.grid) and 0 <= col < len(self.grid[0]):
                self.grid[row][col] = 4
        
        # positions
        for row, col in self.states:
            if 0 <= row < len(self.grid) and 0 <= col < len(self.grid[0]):
                self.grid[row][col] = 1 
            if (row, col) == (self.states[0]):
                self.grid[row][col] = 2 
            if (row, col) == (self.states[-1]):
                self.grid[row][col] = 3
            
            
        FPS = 30
        timer = pygame.time.Clock()
        done = True        
        while done:
            for evento in pygame.event.get(): 
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
       
                elif evento.type == 768:
                    done = False
                                    
                                    
            janela.fill(BLACK)
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
                
                    pygame.draw.rect(janela, cor, [(self.margin + self.width) * col + self.margin,
                    (self.margin + self.height) * row + self.margin, self.width, self.height])
                    
                    
            timer.tick(FPS)
            pygame.display.flip()
