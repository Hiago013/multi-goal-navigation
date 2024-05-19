from environment import path_view
from targets import multi_goal_position, goal_position
from environment import transition_orientation
from metrics import states_positions, multi_curve, multi_distance, multi_planning, multi_planningtime, multi_allmetrics
from target_state import multi_target
from states import multi_pose_state
import numpy as np

def main():
    """
    The function `main()` creates a grid instance with specified dimensions and states, displays it, and
    saves it to a text file.
    """
    
    targets = [(1, 1), (3, 3)]#[(5, 1), (1, 7), (4,5), (7,9)]
    goal = multi_goal_position(targets)
    state_repr = multi_pose_state(0, 0, 0, 11, 11, 4, targets)
    
    mtarget = multi_target(goal, state_repr)
    
    curves = multi_allmetrics.run(np.load('qtable.npy'), mtarget, (0 , 0 , 1, 0, 0, ), transition_orientation)
    print(curves)
    
    states = states_positions.run(qtable=np.load('qtable.npy'), target_state=goal,
                                   start_state=(0, 0, 1, 0, 0), trans_model=transition_orientation)
    
    
    
    
    
    
    
    grid_instance = path_view(5, 5, 50, 50, states=states)
    grid_instance.main()
    grid_instance.save('environment/maps/path.txt')

if __name__== "__main__":
    main()