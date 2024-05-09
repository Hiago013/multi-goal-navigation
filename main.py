from intelligence import qlearning
from environment import gridworld, load_obstacles
import numpy as np
import matplotlib.pyplot as plt

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
    plt.plot(rewards)
    plt.show()


main(8, 8, 4, 3, 60000)