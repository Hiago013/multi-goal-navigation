from .metrics_interface import metrics_interface
from environment.src import transition_orientation
from targets import goal_position
import numpy as np
from typing import Tuple,List

# This class likely implements a success rate metric and inherits from a metrics interface.
class success_rate(metrics_interface):
    @staticmethod
    def run(states:List[Tuple[int,int,int]], qtable:np.ndarray,
            goal:goal_position, trans_model:transition_orientation): # goal_position add
        
        count = 0 # conta qnts estados convergem
        row, col, psi = qtable.shape[0:-1]
        visit = np.zeros((row,col,psi))
        for state in states:
            if visit[state] == 1:     
                count += 1
                continue
            elif visit[state] == -1:
                continue
            done = False
            max_step = 0
            next_state = state
            state_list  = [state]
            while not done and max_step < 30:
                best_action = np.argmax(qtable[next_state])
                next_state = trans_model.step(next_state, best_action)
                state_list.append(next_state)
                max_step += 1
                if goal.isdone(next_state):
                    count += 1
                    done = True

            if done:
                for step in state_list:
                    visit[step] = 1
            else:
                for step in state_list:
                    visit[step] = -1

        return 100*count/len(states)

