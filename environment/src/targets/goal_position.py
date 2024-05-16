from .target_interface import target_interface
from typing import Tuple

# This class defines a goal position that implements a target interface.
class goal_position(target_interface):
    def __init__(self, goal: Tuple):
        assert len(goal) > 1, 'Tuple length must be greater then 1'
        self.__goal = goal

    def isdone(self, state: Tuple[int, int, int]) -> bool:
        return (state[0], state[1]) == self.__goal

    def get_goal(self):
        return self.__goal