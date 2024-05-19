from .multi_metrics_interface import multi_metrics_interface
from environment.src import transition_orientation
from target_state import multi_target
from typing import Tuple
import numpy as np

# This class likely represents a collection of curves and implements methods defined in the `metrics_interface`.
class multi_curve(multi_metrics_interface):
    def run( qtable : np.ndarray,
            target_state : multi_target,
            start_state : Tuple,
            trans_model : transition_orientation):
        
        turns = 0
        n = 500
        next_state = start_state
        next_pose = (start_state[0], start_state[1], start_state[2])
        while not(target_state.isdone(next_pose)) and n > 0:
            best_action = np.argmax(qtable[next_state])
            next_pose = trans_model.step(next_pose, best_action)
            _ = target_state.isgoal(next_pose)
            next_state = target_state.pose2state(next_pose)
            if best_action != 0:
                turns += 1
            n -= 1
        target_state.reset()
        return turns




