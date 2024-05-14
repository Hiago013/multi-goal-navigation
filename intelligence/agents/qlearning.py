import numpy as np
from typing import Union, Type, Tuple
from .egreedy_decay import egreedy_decay
from .egreedy_classic import egreedy_classic
class qlearning():
    def __init__(self, alpha : float, gamma : float, epsilon : float,
                 row : int, col : int, psi : int, actions : int,
                 exploration  : Union[Type[egreedy_decay], None] = None):
        """
        This function initializes the parameters and Q-table for a reinforcement learning algorithm.
        """
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.actions = actions
        self.Q = np.zeros((row, col, psi, actions))

        if exploration is None:
            self.exploration = egreedy_classic(0.1)
        else:
            self.exploration = exploration

    def save_qtable(self):
        """
        This function saves the Q-table as a numpy file named 'qtable.npy'.
        """
        np.save('qtable.npy', self.Q)


    def update_q(self, s:Tuple[int, int, int], a:int, r:float,
                 s_prime:Tuple[int, int, int]):
        """
        This function updates the Q-value in a Q-learning algorithm based on the current state, action,
        reward, next state, learning rate (alpha), and discount factor (gamma).
        """
        row, col, psi = s
        row_prime, col_prime, psi_prime = s_prime
        self.Q[row, col, psi ,a] = self.Q[row, col, psi ,a] + self.alpha*\
            (r + self.gamma*np.max(self.Q[row_prime, col_prime, psi_prime])- self.Q[row, col, psi ,a])


    def action(self, state:Tuple[int, int, int], t:int):
        """
        This function selects an action based on epsilon-greedy policy using a Q-table.
        """
        action = self.exploration.choose_action(t, self.actions, state, self.Q)
        return action