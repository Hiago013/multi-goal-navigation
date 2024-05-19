from .metrics_interface import metrics_interface
from environment.src import transition_orientation
from targets import goal_position
from typing import Tuple
import numpy as np

# This class likely represents a module for calculating distances and implements methods defined in a metrics interface.
class distances(metrics_interface):
    def run(qtable,
            target_state:goal_position,
            start_state:Tuple,
            trans_model:transition_orientation):
        dist = 0
        n = 500
        next_state = start_state
        while not(target_state.isdone(next_state)) and n > 0:
            best_action = np.argmax(qtable[next_state])
            next_state = trans_model.step(next_state, best_action)
            if best_action == 0:
                dist += 1
            n -= 1
        return dist


