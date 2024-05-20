from factory import agent_const_epsilon as agent
from factory import env_multigoal_pose as env
from factory import grid_agent

class factory_context:
    @staticmethod
    def run(n_row, n_col, n_psi, n_action, targets, alpha=0.1, gamma=0.99, epsilon=0.1):
        intelligence = agent.create(alpha, gamma, epsilon, n_action, n_row, n_col, n_psi, targets)
        environment = env.create(n_row, n_col, n_psi, targets)
        context = grid_agent(intelligence, environment)
        return context