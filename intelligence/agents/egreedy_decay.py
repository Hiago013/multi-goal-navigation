from .exploration_interface import exploration_interface
import numpy as np

class egreedy_decay(exploration_interface):
    def __init__(self, initial_value, angular_decay):
        self.initial_value = initial_value
        self.angular_decay = angular_decay

    def choose_action(self, t, n_actions, state, qtable):
        epsilon = self.initial_value + self.angular_decay * t

        epsilon = max(0.01, epsilon)

        row, col, psi = state
        if np.random.rand(1)[0] < epsilon:
            a = np.random.randint(0, n_actions)
        else:
            a = np.argmax(qtable[row, col, psi])
        return a

