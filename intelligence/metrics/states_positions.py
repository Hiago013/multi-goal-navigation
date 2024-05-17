from .metrics_interface import metrics_interface
from environment.src import goal_position, transition_position
from typing import Tuple, List
import numpy as np

class states_positions(metrics_interface):
    @staticmethod
    def run(qtable,
            target_state: goal_position,
            start_state: Tuple,
            trans_model: transition_position,
            ) -> List[Tuple[int, int]]:

        n = 500
        next_state = start_state
        states = [(start_state[0],start_state[1])]
        while not(target_state.isdone(next_state)) and n > 0:
            best_action = np.argmax(qtable[next_state])
            row, col = next_state[0], next_state[1]
            next_state = trans_model.step((row, col), best_action)
            if best_action == 0:
                states.append(tuple([next_state[0], next_state[1]]))
            n -= 1

        return states
