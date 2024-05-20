from factory import agent_const_epsilon as agent
from factory import env_multigoal_pose as env
from factory import grid_agent
from time import time

def main(n_row, n_col, n_psi, n_action, targets, alpha=0.1, gamma=0.99, epsilon=0.1):
    intelligence = agent.create(alpha, gamma, epsilon, n_action, n_row, n_col, n_psi, targets)
    environment = env.create(n_row, n_col, n_psi, targets)
    context = grid_agent(intelligence, environment)
    
    init = time()
    context.train(80000)
    fim = time()
    start = (0, 0, 0, 0, 0, 0, 0)
    context.get_stats(start)
    print(f'Training time: {fim - init}')
    context.show(start)
    
    
    

main(11, 11, 4, 3, [(5, 1), (4, 5), (1, 7), (7, 9)], epsilon=.2)