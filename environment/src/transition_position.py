from .model_transition_interface import model_trasition_interface
import numpy as np

class transition_position(model_trasition_interface):
    @staticmethod
    def step(state, action):
        """
        The function `model_trans` takes a state and an action as input and returns a new state based on the
        action taken in a simple 2D grid world with four possible actions.
        """
        position_transition = np.array([[1, 0],  
                                        [0, 1],  
                                        [-1, 0],  
                                        [0, -1]])  
        
        row, col = state
        if action >= 0 and action < len(position_transition):   #[0,1,2,3]
            new_position = position_transition[action] + np.array([row, col])
            new_state = tuple(new_position)
        else:
            new_state = state
            
        return new_state
        
        