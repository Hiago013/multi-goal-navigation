from .multi_metrics_interface import multi_metrics_interface
from environment.src import transition_orientation
from target_state import multi_target
from typing import Tuple, Dict
import numpy as np
from time import time

# This class likely represents a collection of curves and implements methods defined in the `metrics_interface`.
class multi_allmetrics(multi_metrics_interface):
    def run( qtable : np.ndarray,
            target_state : multi_target,
            start_state : Tuple,
            trans_model : transition_orientation) -> Dict:

        n = 100
        turns = 0
        next_state = start_state
        next_pose = (start_state[0], start_state[1], start_state[2])
        path = [next_pose[0:2]]
        metrics = {'curve': 0,
                       'distance': 0,
                       'runtime': 0,
                       'path': path}
        start = time()
        while not(target_state.isdone(next_pose)) and n > 0:
            best_action = np.argmax(qtable[next_state])
            next_pose = trans_model.step(next_pose, best_action)
            _ = target_state.isgoal(next_pose)
            next_state = target_state.pose2state(next_pose)
            if best_action == 0:
                metrics['path'].append(next_pose[0:2])
                metrics['distance'] += 1
            elif best_action != 0 and metrics['distance'] > 0: # if the agent is already on a curve
                metrics['curve'] += 1
        ending = time()
        metrics['runtime'] = (ending - start) * 1000
        target_state.reset()
        return metrics




