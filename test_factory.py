from factory import agent_const_epsilon as agent
from factory import env_multigoal_pose as env
from factory import grid_agent
from time import time

def main(n_row, n_col, n_psi, n_action, targets, alpha=0.1, gamma=0.99, epsilon=0.1):
    intelligence = agent.create(alpha, gamma, epsilon, n_action, n_row, n_col, n_psi, targets)
    environment = env.create(n_row, n_col, n_psi, targets)
    context = grid_agent(intelligence, environment)

   # init = time()
   # context.train(50000, show=False)
   # fim = time()
    start = (15, 9, 2, 0, 0, 0, 0)
    context.get_stats(start)
   # print(f'Training time: {(fim - init):.2f}')
    context.show(start)




main(16, 10, 4, 3, [(3, 2), (5, 8), (8, 2), (12, 5)])