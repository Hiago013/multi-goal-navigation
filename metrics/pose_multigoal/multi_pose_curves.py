from .metrics_interface import metrics_interface
from environment.src import multi_goal_position, transition_orientation
from typing import Tuple
import numpy as np

# This class likely represents a collection of curves and implements methods defined in the `metrics_interface`.
class multi_pose_curves(metrics_interface):
    def run(qtable,
            target_state:multi_goal_position,
            start_state:Tuple,
            trans_model: transition_orientation):
        
        turns = 0
        n = 50 # Max attempts number
        next_state = start_state
        
        while not(target_state.isdone(next_state)) and n > 0:
            best_action = np.argmax(qtable[next_state])
            next_pose = trans_model.step(next_state, best_action)
            
            if best_action != 0:
                turns += 1
            n -= 1
        return turns




