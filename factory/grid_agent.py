import numpy as np
import matplotlib.pyplot as plt
from environment import gridworld_multigoal, path_view
from intelligence import qlearning
from metrics.pose_multigoal import multi_planning, multi_allmetrics
from environment.src.transition_models import transition_orientation


class grid_agent():
    def __init__(self, intelligence : qlearning, environment : gridworld_multigoal):
        self.__intelligence = intelligence
        self.__environment = environment
        self.__row = environment.nrow
        self.__col = environment.ncol
        self.__psi = environment.n_psi
        
        self.start_state = tuple([0 for _ in self.__environment.target_state_repr.get_shape()])
    
    def train(self, episodes, save = True, show = True):
        rewards = np.zeros(episodes)
        for episode in range(episodes):
            print('Episode:', episode, end='\r')
            rr = 0
            while not self.__environment.isdone():
                s = self.__environment.getState()
                a = self.__intelligence.action(s, episode)
                s, a, r, s_prime = self.__environment.step(a)
                self.__intelligence.update_q(s,a,r,s_prime)
                rr += r
            rewards[episode] = rr
            self.__environment.reset()
            self.__environment.exploring_starts()
        if save:
            self.__intelligence.save_qtable()
        if show:
            plt.plot(rewards)
            plt.show()
    
    def show(self, start_state = None):
        if not start_state:
            start_state= self.start_state 
        path = multi_planning.run(np.load('qtable.npy'), self.__environment.target_state_repr, start_state, transition_orientation)
        pv = path_view(self.__row, self.__col, path)
        pv.run()
    
    def get_stats(self, start_state = None) :
        if not start_state:
            start_state= self.start_state 
        metrics = multi_allmetrics.run(np.load('qtable.npy'), self.__environment.target_state_repr, start_state, transition_orientation)
        metrics['runtime']
        print(f'----------------------- Stats Starting in the state {start_state} -----------------------')
        print(f'Planning time: {metrics["runtime"]:.2f} (ms)')
        print(f'Distance: {metrics["distance"]} (m)')
        print(f'Number of turns: {metrics["curve"]}')
            