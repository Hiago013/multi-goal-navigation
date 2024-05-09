import numpy as np
from typing import Tuple, List
class gridworld(object):
    def __init__(self, nrow, ncol, r_g, c_g):
        self.c_r = 0
        self.c_c = 0
        self.c_psi = 0

        self.nrow = nrow
        self.ncol = ncol

        self.goal = np.array([r_g, c_g])
        self.obstacles = np.array([])

        self.n_psi = 4

        self.psi_transition = np.array([0, 1, -1])
        self.position_transition = np.array([[1, 0],
                  [0, 1],
                  [-1, 0],
                  [0, -1]])


    def set_obstacles(self, obstacles:List[Tuple[int, int]]):
        self.obstacles = np.array(obstacles)

    def getReward(self, s:Tuple[int, int]):
        r = -1
        if np.all(self.goal == np.array([s[0], s[1]])):
            r += 100

        for i in range(len(self.obstacles)):
            if np.all(self.obstacles[i] == s):
                r += -5
                break
        return r

    def isdone(self):
        if np.all(self.goal == np.array([self.c_r, self.c_c])):
            return True
        return False

    def step(self, a):
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
        r = self.getReward(new_position)

        return s,a,r,s_prime

    def getState(self):
        return np.array([self.c_r, self.c_c, self.c_psi])

    def reset(self):
        self.c_r = 0
        self.c_c = 0
        self.c_psi = 0

    def exploring_starts(self):
        self.c_r = np.random.randint(self.nrow)
        self.c_c = np.random.randint(self.ncol)
        self.c_psi = np.random.randint(self.n_psi)