from intelligence import qlearning, success_rate, all_metrics
from environment import gridworld, load_obstacles
import numpy as np
import matplotlib.pyplot as plt

def model_trans(state, action):
    """
    The function `model_trans` takes a state and an action as input and returns a new state based on the
    action taken in a simple 2D grid world with four possible actions.
    """
    psi_transition = np.array([0, 1, -1])
    position_transition = np.array([[1, 0],
                  [0, 1],
                  [-1, 0],
                  [0, -1]])
    
    position = state[0:2]
    psi = state[-1]
    
    if action == 0:
        new_position = position_transition[psi] + position
        new_psi = psi
    else:
        new_position = position
        new_psi = (psi + psi_transition[action]) % 4
    
    new_state = tuple([new_position[0], new_position[1], new_psi])
    return new_state



def main(n_row, n_col, n_psi, n_action, n_episodes):
    """
    The main function implements Q-learning algorithm to train an agent in a gridworld environment with
    obstacles and plots the rewards obtained over multiple episodes.
    """
    agent = qlearning(0.1, 0.99, 0.1, n_row, n_col, n_psi, n_action)
    env = gridworld(n_row, n_col, n_row - 1, n_col - 1)
    obs = load_obstacles().load('environment/maps/map.txt')
    env.set_obstacles(obs)

    rewards = np.zeros(n_episodes)
    for episode in range(n_episodes):
        rr = 0
        while not env.isdone():
            s = env.getState()
            a = agent.action(s)
            s, a, r, s_prime = env.step(a)
            agent.update_q(s,a,r,s_prime)
            rr += r
        rewards[episode] = rr
        env.reset()
        env.exploring_starts()
    agent.save_qtable()
    
    states = [(0, 0, 0), (0, 1, 0), (3,3,0)]  
    sr = success_rate.run(states, np.load('qtable.npy'), tuple(env.goal), model_trans)
    curves, dist, time = all_metrics.run(qtable=np.load('qtable.npy'), target_state=tuple(env.goal), trans_model=model_trans)
    
    print("Success rate:", sr)
    print(f'{curves, dist, time}')
    plt.plot(rewards)
    plt.show()


main(5, 5, 4, 3, 1000)