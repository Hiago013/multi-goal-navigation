from metrics_interface import metrics_interface
import numpy as np
from typing import Tuple,List

class success_rate(metrics_interface):
    @staticmethod
    def run(states:List[Tuple[int,int,int]], qtable:np.ndarray,
            goal:Tuple[int,int], trans_model):
        count = 0 # conta qnts estados convergem
        row, col, psi = qtable.shape[0:-1]
        visit = np.zeros((row,col,psi))
        for state in states:
            if visit[state] == 1:      #or np.any(qtable[state] == 1):
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
                next_state = trans_model(next_state, best_action)
                state_list.append(next_state)
                max_step += 1
                if (next_state[0], next_state[1]) == goal:
                    count += 1
                    done = True
            
            if done:
                visit[state_list] = 1
            else:
                visit[state_list] = -1
                
        return 100*count/len(states)


states = [(0, 0, 0), (0, 1, 0)]  
qtable = np.zeros((2, 2, 4, 4))  
goal = (1, 1)  
sr = success_rate().run(states, qtable, goal)
print("Succes rate:", sr)