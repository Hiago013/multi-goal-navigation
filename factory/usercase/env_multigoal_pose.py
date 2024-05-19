from environment import gridworld_multigoal
from target_state import multi_target
from states import multi_pose_state
from targets import multi_goal_position
from environment.src import transition_orientation
from .factory_interface import factory_interface
from environment.src import load_obstacles
class env_multigoal_pose(factory_interface):
    @staticmethod
    def create(n_row, n_col, n_psi, targets):

        state_repr = multi_pose_state(0, 0, 0, n_row, n_col, n_psi, targets)
        goal = multi_goal_position(targets)
        multi_target_gd = multi_target(goal, state_repr)
        
        env =  gridworld_multigoal(n_row, n_col, transition_orientation, multi_target_gd)
        obs = load_obstacles().load('environment/maps/map.txt')
        env.set_obstacles(obs)
        
        return env