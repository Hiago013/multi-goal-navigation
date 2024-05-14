import numpy as np
from typing import Tuple, List
from .goal_position import goal_position
class gridworld(object):
    def __init__(self, nrow, ncol, goal:goal_position):
        """
        This function initializes variables for a grid environment with a specified number of rows and
        columns, a goal position, and transition matrices for position and orientation.
        """
        self.c_r = 0
        self.c_c = 0
        self.c_psi = 0

        self.nrow = nrow
        self.ncol = ncol

        self.goal = goal
        self.obstacles = np.array([])

        self.n_psi = 4

        self.psi_transition = np.array([0, 1, -1])
        self.position_transition = np.array([[1, 0],
                  [0, 1],
                  [-1, 0],
                  [0, -1]])


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
        #print(s)
        if self.goal.isdone(s):
            r += 100

        for i in range(len(self.obstacles)):
            if np.all(self.obstacles[i] == s[0:2]):
                r += -5
                break
        return r

    def isdone(self):
        """
        The function `isdone` checks if the current position (`c_r`, `c_c`) matches the goal position.
        """
        if self.goal.isdone((self.c_r, self.c_c, self.c_psi)):
            return True
        return False

    def step(self, a):
        """
        The function `step` updates the position and orientation of an agent based on the action taken
        and returns the state, action, reward, and next state.
        """
        position = np.array([self.c_r, self.c_c])
        psi = self.c_psi

        s = np.array([self.c_r, self.c_c, self.c_psi])

        if a == 0:
          new_position = self.position_transition[psi] + position
          new_psi = psi
        else:
          new_position = position
          new_psi = (psi + self.psi_transition[a]) % self.n_psi


        if not ((new_position >= 0).all() and (new_position[0] < self.nrow) and
                (new_position[1] < self.ncol)):
            new_position = position

        self.c_r = new_position[0]
        self.c_c = new_position[1]
        self.c_psi = new_psi

        s_prime = np.array([self.c_r, self.c_c, self.c_psi])
        r = self.getReward(tuple(s_prime))

        return s,a,r,s_prime

    def getState(self):
        """
        The function `getState` returns a NumPy array containing the values of `c_r`, `c_c`, and
        `c_psi`.
        """
        return np.array([self.c_r, self.c_c, self.c_psi])

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