import pygame
import sys
from typing import Tuple, List

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
                color = self._get_color(model.get_cell_value(row, col))
                pygame.draw.rect(window, color, [(self.margin + self.width) * col + self.margin,
                                                  (self.margin + self.height) * row + self.margin,
                                                  self.width, self.height])

    def _get_color(self, value: int) -> Tuple[int, int, int]:
        if value == 1:
            return YELLOW
        elif value == 2:
            return RED
        elif value == 3:
            return GREEN
        else:
            return WHITE

class GameController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def update_model(self, row: int, col: int, value: int):
        self.model.set_cell(row, col, value)

class PathPlanningApp:
    def __init__(self, row: int, col: int, width: int, height: int, margin: int, states: List[Tuple[int, int]]):
        self.model = GridModel(row, col)
        self.view = GridView(row, col, width, height, margin)
        self.controller = GameController(self.model, self.view)
        self.view.states = states

    def run(self):
        pygame.init()
        window = pygame.display.set_mode(((self.view.col * self.view.height) + self.view.col + 1,
                                          (self.view.row * self.view.width) + self.view.row + 1))
        pygame.display.set_caption("Path Planning")
        while True:
            self.controller.handle_events()
            self.view.draw_grid(window, self.model)
            pygame.display.flip()

if __name__ == "__main__":
    # Example usage
    states = [(1, 2), (3, 4)]  # Example states
    app = PathPlanningApp(10, 10, 30, 30, 1, states)
    app.run()
