from .state_interface import state_interface
from typing import Tuple

class pose_state(state_interface):
    def __init__(self, row:int, col:int, psi:int, max_row:int, max_col:int, max_psi) -> None:
        """
        This function initializes the row and column of an agent in a grid environment.
        """
        self.row = row
        self.col = col
        self.psi = psi
        self.shape : Tuple[int, int, int] = (max_row, max_col, max_psi)

    def getState(self) -> Tuple[int, int]:
        """
        The function `getState` returns the current state of an agent in a grid environment.
        """
        return (self.row, self.col, self.psi)

    def setState(self, s : Tuple[int, int, int]) -> None:
        """
        The function `setState` sets the state of an agent in a grid environment.
        """
        self.row = s[0]
        self.col = s[1]
        self.psi = s[2]

    def getShape(self) -> Tuple[int, int, int]:
        return self.shape
