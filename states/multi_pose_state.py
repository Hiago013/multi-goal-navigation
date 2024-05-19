from.multi_state_interface import multi_state_interface
from typing import Tuple, List

class multi_pose_state(multi_state_interface):
    def __init__(self, row:int, col:int, psi:int,
                 max_row:int, max_col:int, max_psi:int,
                 targets:List[Tuple[int, int]]) -> None:
        """
        This function initializes the row and column of an agent in a grid environment.
        """
        self.row = row
        self.col = col
        self.psi = psi
        self.targets = targets
        self.n_targets = len(targets)
        self.visited = [0] * (self.n_targets)

        self.shape = [max_row, max_col, max_psi]
        for _ in range(self.n_targets):
            self.shape.append(2)

    def getState(self) -> Tuple[int, int]:
        """
        The function `getState` returns the current state of an agent in a grid environment.
        """
        state = [self.row, self.col, self.psi]
        state.extend(self.visited)
        return tuple(state)

    def setState(self, s : Tuple[int, int, int]) -> None:
        """
        The function `setState` sets the state of an agent in a grid environment.
        """
        self.row = s[0]
        self.col = s[1]
        self.psi = s[2]
        self.visited = s[3:]

    def getShape(self) -> Tuple[int, int, int]:
        return self.shape

    def getTargets(self) -> List[Tuple[int, int]]:
        return self.targets

    def reset(self) -> None:
        self.visited = [0] * self.n_targets
