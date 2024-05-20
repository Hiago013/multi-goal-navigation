from intelligence import qlearning, egreedy_decay
from states import multi_pose_state
from .factory_interface import factory_interface

class agent_const_epsilon(factory_interface):
    @staticmethod
    def create(alpha, gamma, epsilon, n_action, n_row, n_col, n_psi, targets) -> qlearning:
        state_repr = multi_pose_state(0, 0, 0, n_row, n_col, n_psi, targets)

        return qlearning(alpha, gamma, epsilon, state_repr, n_action, egreedy_decay(1, -0.9/50000))


