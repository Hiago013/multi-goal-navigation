from .target_interface import target_interface
from typing import Tuple, List

# This class defines a goal position that implements a target interface.
class multi_goal_position(target_interface):
    def __init__(self, goal: List[Tuple[int, int]]):
        assert len(goal) > 1, 'Tuple length must be greater then 1'
        self.__goal : List[Tuple[int, int]] = goal
        self.__visitados : set = {}

    def isdone(self, state: Tuple[int, int, int]) -> bool:
        new_state = (state[0], state[1])
        if new_state in self.__goal:
            self.__visitados.add(new_state)
        return self.__doneiscompleted()

    def isgoal(self, state: Tuple[int, int, int]) -> bool:
        new_state = (state[0], state[1])
        if (new_state in self.__goal) and not (new_state in self.__visitados):
            return True
        return False

    def __doneiscompleted(self):
        return len(self.__visitados) == len(self.__goal)

    def get_goal(self):
        return self.__goal