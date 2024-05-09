
from metrics_interface import metrics_interface
from typing import Tuple
import numpy as np

# This class likely represents a collection of curves and implements methods defined in the `metrics_interface`.
class curves(metrics_interface):
    def run(self, qtable,
            target_state:Tuple[int, int, int],
            trans_model):
        turns = 0
        n = 500
        start_state = (0, 0, 0)
        next_state = (0, 0, 0)
        while (next_state != target_state) and n > 0:
            best_action = np.argmax(qtable[start_state])
            next_state = trans_model(start_state, best_action)
            if best_action != 0:
                turns += 1
            n -= 1
        return turns
    
        
        

