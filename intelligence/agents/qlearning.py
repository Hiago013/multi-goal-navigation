import numpy as np
from typing import Tuple
class qlearning():
    def __init__(self, alpha : float, gamma : float, epsilon : float,
                 row : int, col : int, psi : int, actions : int):

        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.actions = actions
        self.Q = np.zeros((row, col, psi, actions))

    def update_q(self, s:Tuple[int, int, int], a:int, r:float,
                 s_prime:Tuple[int, int, int]):

        row, col, psi = s
        row_prime, col_prime, psi_prime = s_prime
        self.Q[row, col, psi ,a] = self.Q[row, col, psi ,a] + self.alpha*\
            (r + self.gamma*np.max(self.Q[row_prime, col_prime, psi_prime])- self.Q[row, col, psi ,a])

    def action(self, s:Tuple[int, int, int]):
        row, col, psi = s
        if np.random.rand(1)[0] < self.epsilon:
            a = np.random.randint(0, self.actions)
        else:
            a = np.argmax(self.Q[row, col, psi])
        return a