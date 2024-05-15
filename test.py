from intelligence import qlearning, success_rate, all_metrics, egreedy_decay
from environment import gridworld, load_obstacles, goal_position, goal_orientation
from environment import transition_orientation as trans_model
from dictionary_position import dictionary_position
from environment import transition_position
import numpy as np
import matplotlib.pyplot as plt


def main(n_row, n_col, n_psi, n_action, n_episodes):
    """
    The main function implements Q-learning algorithm to train an agent in a gridworld environment with
    obstacles and plots the rewards obtained over multiple episodes.
    """
    agent = qlearning(0.1, 0.99, 0.1, n_row, n_col, n_psi, n_action, exploration=egreedy_decay(1, -.001))
    goal = goal_position((4, 4))
    env = gridworld(n_row, n_col, goal)
    obs = load_obstacles().load('environment/maps/map.txt')
    env.set_obstacles(obs)
    
    rewards = np.zeros(n_episodes)
    for episode in range(n_episodes):
        rr = 0
        while not env.isdone():
            s = env.getState()
            a = agent.action(s, episode)
            s, a, r, s_prime = env.step(a)
            agent.update_q(s,a,r,s_prime)
            rr += r
        rewards[episode] = rr
        env.reset()
        env.exploring_starts()
    agent.save_qtable()

    states = [(0, 0, 0), (0, 1, 0), (3,3,0)]
    sr = success_rate.run(states=states, qtable=np.load('qtable.npy'),
                         goal=env.goal, trans_model=trans_model)
    curves, dist, time = all_metrics.run(qtable=np.load('qtable.npy'), target_state=env.goal,
                                         start_state=(0,0,0), trans_model=trans_model)
    print("Success rate:", sr)
    print(f'Curves:{curves}   Dist:{dist}   Time:{time:.5f}s\n')
    plt.plot(rewards)
    plt.show()
    
    dicti = dictionary_position(nrow=5, ncol=5, modelo=transition_position, actions=[0, 1, 2, 3])
    graph = dicti.dict2D()
    for state in graph:
        print(f'{state} : {graph[state]}')

main(5, 5, 4, 3, 1000)

