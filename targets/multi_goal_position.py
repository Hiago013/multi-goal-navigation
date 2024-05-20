from .target_interface import target_interface
from typing import Tuple, List

# This class defines a goal position that implements a target interface.
class multi_goal_position(target_interface):
    def __init__(self, goal: List[Tuple[int, int]]):
        assert len(goal) > 1, 'Tuple length must be greater then 1'
        self.__goal : List[Tuple[int, int]] = goal
        self.__visitados : set = set()
        self.visited_state = dict(zip(goal, [0]*len(goal)))

    def isdone(self, state: Tuple[int, int, int]) -> bool:
        return self.__doneiscompleted()

    def isgoal(self, state: Tuple[int, int, int]) -> bool:
        new_state = (state[0], state[1])
        if (new_state in self.__goal) and not (new_state in self.__visitados):
            self.__visitados.add(new_state)
            self.__update_state(new_state)
            return True
        return False

    def get_goal(self):
        return self.__goal

    def get_visited_state(self):
        return list(self.visited_state.values())

    def set_visited_state(self, state: List[int]):
        self.visited_state = dict(zip(self.__goal, state))
        self.__visitados = set([k for k, v in self.visited_state.items() if v == 1])

    def reset(self):
        self.__visitados.clear()
        self.visited_state = dict(zip(self.__goal,
                                      [0]*len(self.__goal)))

    def __doneiscompleted(self):
        return len(self.__visitados) == len(self.__goal)

    def __update_state(self, state: Tuple[int, int]):
        self.visited_state[state] = 1
