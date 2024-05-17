from .state_interface import state_interface
from typing import Tuple

class position_state(state_interface):
    def __init__(self, row:int, col:int, max_row:int, max_col:int) -> None:
        """
        This function initializes the row and column of an agent in a grid environment.
        """
        self.row = row
        self.col = col
        self.shape : Tuple[int, int] = (max_row, max_col)

    def getState(self) -> Tuple[int, int]:
        """
        The function `getState` returns the current state of an agent in a grid environment.
        """
        return (self.row, self.col)

    def setState(self, s : Tuple[int, int]) -> None:
        """
        The function `setState` sets the state of an agent in a grid environment.
        """
        self.row = s[0]
        self.col = s[1]

    def getShape(self) -> Tuple[int, int]:
        return self.shape
