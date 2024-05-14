from .exploration_interface import exploration_interface
import numpy as np

class egreedy_classic(exploration_interface):
    def __init__(self, epsilon):
        self.epsilon = epsilon

    def choose_action(self, t, n_actions, state, qtable):
        row, col, psi = state
        if np.random.rand(1)[0] < self.epsilon:
            a = np.random.randint(0, n_actions)
        else:
            a = np.argmax(qtable[row, col, psi])
        return a

