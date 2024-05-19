from .metrics_interface import metrics_interface
from environment.src import transition_orientation
from targets import goal_position
from typing import Tuple
import numpy as np
from time import time


# This class is implementing all the methods defined in the `metrics_interface` interface.
class all_metrics(metrics_interface):
    @staticmethod
    def run( qtable,
            target_state:goal_position,
            start_state:Tuple,
            trans_model:transition_orientation):
        turns = 0
        dist = 0
        n = 500
        next_state = start_state
        start_time = time()
        while not(target_state.isdone(next_state)) and n > 0:
            best_action = np.argmax(qtable[next_state])
            next_state = trans_model.step(next_state, best_action)
            if best_action != 0:
                turns += 1
            else:
                dist += 1
            n -= 1
        final_time = time() - start_time
        return turns, dist, final_time
