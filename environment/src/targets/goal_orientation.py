from .target_interface import target_interface
from typing import Tuple

# This class represents a goal orientation and implements a target interface.
class goal_orientation(target_interface):
    def __init__(self, goal: Tuple):
        assert len(goal) > 2, 'Tuple length must be greater then 2'
        self.__goal = goal

    def isdone(self, state: Tuple[int, int, int]) -> bool:
        return (state[0], state[1], state[2]) == self.__goal

    def get_goal(self):
        return self.__goal