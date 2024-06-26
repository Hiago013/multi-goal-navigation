from factory import agent_const_epsilon as agent
from factory import env_multigoal_pose as env
from factory import grid_agent
from time import time
import pandas as pd
import numpy as np

def main(n_row, n_col, n_psi, n_action, targets, alpha=0.1, gamma=0.99, epsilon=0.1):
    data_header = ['Planning time', 'Path length', 'Curves', 'Success rate', 'Training time']
    start = (0, 0, 0, 0, 0, 0, 0)
    for i in range(1, 21):
        data_deploy = []
        intelligence = agent.create(alpha, gamma, epsilon, n_action, n_row, n_col, n_psi, targets)
        environment = env.create(n_row, n_col, n_psi, targets)
        context = grid_agent(intelligence, environment)
        init = time()
        rewards = context.train(50000, show=False)
        fim = time()
        for r in range(n_row):
            for c in range(n_col):
                for p in range(n_psi):
                    if not environment.obstaclemap[r,c]:
                        start = (r, c, p, 0, 0, 0, 0)
                        values = context.get_stats(start)
                        data_deploy.append(values)
        data_deploy_df = pd.DataFrame(data_deploy)
        data_deploy_df[3] = context.get_success_rate()[0]
        data_deploy_df[4] = fim - init
        data_deploy_df.columns = data_header
        data_deploy_df.to_excel(f'data_training/map_2/data_deploy_{i}.xlsx')
        np.save(f'data_training/map_2/rewards_{i}.npy', rewards)
        print(f'{i}th Training time: {(fim - init):.2f}')
        context.show(start)




main(16, 10, 4, 3, [(3, 4), (7, 7), (10, 1), (13, 7)])