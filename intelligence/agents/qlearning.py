import numpy as np
from typing import Union, Type, Tuple
from .egreedy_decay import egreedy_decay
from .egreedy_classic import egreedy_classic
from states import pose_state
class qlearning():
    def __init__(self, alpha : float, gamma : float, epsilon : float,
                 state_repr:pose_state, actions : int,
                 exploration  : Union[Type[egreedy_decay], None] = None):
        """
        This function initializes the parameters and Q-table for a reinforcement learning algorithm.
        """
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.actions = actions
        state_action = self.__state_action(state_repr.getShape(), actions)

        self.Q = np.zeros(state_action)

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
        state_action = self.__state_action(s, a)
        self.Q[state_action] = self.Q[state_action] + self.alpha*\
            (r + self.gamma*np.max(self.Q[s_prime])- self.Q[state_action])


    def action(self, state:Tuple[int, int, int], t:int):
        """
        This function selects an action based on epsilon-greedy policy using a Q-table.
        """
        action = self.exploration.choose_action(t, self.actions, state, self.Q)
        return action

    def __state_action(self, state:tuple, action:int):
        """
        This function returns a tuple of state and action.
        """
        state:list = list(state)
        state.append(action)
        state = tuple(state)
        return state