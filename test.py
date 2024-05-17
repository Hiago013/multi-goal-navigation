from intelligence import qlearning, success_rate, all_metrics, egreedy_decay, states_positions
from environment import gridworld, load_obstacles, goal_position, multi_goal_position, gridworld_multigoal
from environment import transition_orientation as trans_model

from states import pose_state, multi_pose_state
from baseline import graph_2d
from environment import transition_position
import numpy as np
import matplotlib.pyplot as plt

def main(n_row, n_col, n_psi, n_action, n_episodes):
    """
    The main function implements Q-learning algorithm to train an agent in a gridworld environment with
    obstacles and plots the rewards obtained over multiple episodes.
    """
    targets = [(3, 3), (2, 2)]
    state_repr = multi_pose_state(0, 0, 0, n_row, n_col, n_psi, targets)
    print(state_repr.getShape())
    agent = qlearning(0.1, 0.99, 0.1, state_repr, n_action)#, exploration=egreedy_decay(1, -0.1/n_episodes))
    goal = multi_goal_position(targets)
    env = gridworld_multigoal(n_row, n_col, goal, trans_model, state_repr)
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

    #states = [(0, 0, 0), (0, 1, 0), (3,3,0)]
    #sr = success_rate.run(states=states, qtable=np.load('qtable.npy'),
    #                     goal=env.goal, trans_model=trans_model)
    #curves, dist, time = all_metrics.run(qtable=np.load('qtable.npy'), target_state=env.goal,
    #                                     start_state=(0,0,0), trans_model=trans_model)
#
    #states = states_positions.run(qtable=np.load('qtable.npy'), target_state=env.goal,
 #                               start_state=(0,0,0), trans_model=trans_model)
  #  print(states)
   # print("Success rate:", sr)
    #print(f'Curves:{curves}   Dist:{dist}   Time:{time:.5f}s\n')

    plt.plot(rewards)
    plt.show()


main(5, 5, 4, 3, 1000)