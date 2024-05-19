from factory import agent_const_epsilon as agent
from factory import env_multigoal_pose as env
from factory import grid_agent

def main(n_row, n_col, n_psi, n_action, targets, alpha=0.1, gamma=0.99, epsilon=0.1):
    intelligence = agent.create(alpha, gamma, epsilon, n_action, n_row, n_col, n_psi, targets)
    environment = env.create(n_row, n_col, n_psi, targets)
    context = grid_agent(intelligence, environment)
    
    context.train(10000)
    context.get_stats()
    context.show((0, 0, 0, 0, 0))
    
    

main(8, 8, 4, 3, [(5, 6), (1, 3), (5, 2)], epsilon=.3)