from .target_interface import target_interface
from typing import Tuple

class goal_position(target_interface):
    def __init__(self, goal: Tuple[int, int]):
        self.__goal = goal

    def isdone(self, state: Tuple[int, int, int]) -> bool:
        return state[0:2] == self.__goal

    def get_goal(self):
        return self.__goal