import numpy as np
from typing import Tuple, List
from targets import goal_position
from .gridworld_interface import gridworld_interface
from ..transition_models import transition_orientation
class gridworld(gridworld_interface):
    def __init__(self, nrow, ncol, goal:goal_position,
                 transition_model : transition_orientation):
        """
        This function initializes variables for a grid environment with a specified number of rows and
        columns, a goal position, and transition matrices for position and orientation.
        """
        self.c_r = 0
        self.c_c = 0
        self.c_psi = 0

        self.nrow = nrow
        self.ncol = ncol
        self.n_psi = 4

        self.goal = goal
        self.obstacles = np.array([])
        self.transition_model = transition_model


    def set_obstacles(self, obstacles:List[Tuple[int, int]]):
        """
        The function `set_obstacles` sets the obstacles for a given object using a list of tuples
        representing coordinates.
        """
        self.obstacles = np.array(obstacles)

    def getReward(self, s:Tuple[int, int, int]):
        """
        The function `getReward` calculates the reward based on the current state `s`, the goal state,
        and obstacles in a grid environment.
        """
        r = -1
        if self.goal.isdone(s):
            r += 100

        for i in range(len(self.obstacles)):
            if np.all(self.obstacles[i] == s[0:2]):
                r += -50
                break
        return r

    def isdone(self):
        """
        The function `isdone` checks if the current position (`c_r`, `c_c`) matches the goal position.
        """
        if self.goal.isdone(self.getState()):
            return True
        return False

    def step(self, a):
        """
        The function `step` updates the position and orientation of an agent based on the action taken
        and returns the state, action, reward, and next state.
        """
        s = self.getState()
        s_prime = self.transition_model.step(s, a)

        if not self.__isingrid((s_prime[0], s_prime[1])):
            s_prime = s

        self.__update_state(s_prime)

        r = self.getReward(s_prime)

        return s, a, r, s_prime

    def getState(self) -> Tuple[int, int, int]:
        """
        The function `getState` returns a NumPy array containing the values of `c_r`, `c_c`, and
        `c_psi`.
        """
        return self.c_r, self.c_c, self.c_psi

    def reset(self):
        """
        The function `reset` resets the values of `c_r`, `c_c`, and `c_psi` to zero
        """
        self.c_r = 0
        self.c_c = 0
        self.c_psi = 0

    def exploring_starts(self):
        """
        The function `exploring_starts` randomly initializes the attributes `c_r`, `c_c`, and `c_psi`
        within specified ranges.
        """
        self.c_r = np.random.randint(self.nrow)
        self.c_c = np.random.randint(self.ncol)
        self.c_psi = np.random.randint(self.n_psi)

    def __isingrid(self, position:Tuple[int, int]) -> bool:
        """
        The function `__isingrid` checks if a given position is within the grid.
        """
        row, col = position
        return (row >= 0) and (col >= 0) and (row < self.nrow) and (col < self.ncol)

    def __update_state(self, s_prime):
        """
        The function `__update_state` updates the current state of the agent.
        """
        self.c_r, self.c_c, self.c_psi = s_prime