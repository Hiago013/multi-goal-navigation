from .metrics_interface import metrics_interface
from environment.src import transition_orientation
from targets import goal_position
from typing import Tuple
import numpy as np
from time import time

# This class named `planning_time` likely implements the `metrics_interface` interface.
class planning_time(metrics_interface):
    def run(qtable,
            target_state:goal_position,
            start_state:Tuple,
            trans_model:transition_orientation):
        n = 500
        next_state = start_state
        start_time = time()
        while (next_state != target_state) and n > 0:
            best_action = np.argmax(qtable[next_state])
            next_state = trans_model.step(next_state, best_action)
            n -= 1
        final_time = time() - start_time
        return final_time
