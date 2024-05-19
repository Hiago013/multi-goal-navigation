from .model_transition_interface import model_trasition_interface
import numpy as np

class transition_orientation(model_trasition_interface):
    @staticmethod
    def step(state, action):
        """
        The function `model_trans` takes a state and an action as input and returns a new state based on the
        action taken in a simple 2D grid world with four possible actions.
        """
        psi_transition = np.array([0, 1, -1])
        position_transition = np.array([[1, 0],
                    [0, 1],
                    [-1, 0],
                    [0, -1]])

        position = (state[0], state[1])
        psi = state[2]

        if action == 0:
            new_position = position_transition[psi] + position
            new_psi = psi
        else:
            new_position = position
            new_psi = (psi + psi_transition[action]) % 4

        new_state = tuple([new_position[0], new_position[1], new_psi])
        return new_state