from environment import path_view, goal_position, multi_goal_position
from environment import transition_orientation
from intelligence import states_positions
import numpy as np

def main():
    """
    The function `main()` creates a grid instance with specified dimensions and states, displays it, and
    saves it to a text file.
    """
    targets = [(3, 3), (2, 2)]
    goal = multi_goal_position(targets)
    states = states_positions.run(qtable=np.load('qtable.npy'), target_state=goal,
                                  start_state=(0, 0, 0, 0, 0), trans_model=transition_orientation)
    grid_instance = path_view(5, 5, 50, 50, states=states)
    grid_instance.main()
    grid_instance.save('environment/maps/path.txt')

if __name__== "__main__":
    main()