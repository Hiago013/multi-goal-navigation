import numpy as np
from typing import Tuple, List
from states import pose_state, multi_pose_state
from .gridworld_interface import gridworld_interface
from targets import multi_goal_position
from ..transition_models import transition_orientation
from target_state import multi_target

class gridworld_multigoal(gridworld_interface):
    def __init__(self, nrow, ncol,
                 transition_model : transition_orientation,
                 target_state_repr: multi_target):
        """
        This function initializes variables for a grid environment with a specified number of rows and
        columns, a goal position, and transition matrices for position and orientation.
        """
        self.c_r = 0
        self.c_c = 0
        self.c_psi = 0

        self.nrow = nrow
        self.ncol = ncol
        self.n_psi = 4


        self.target_state_repr : multi_target = target_state_repr
        self.obstacles = np.array([])
        self.obstaclemap = np.zeros((nrow, ncol), dtype=np.uint8)
        self.transition_model = transition_model

        self.non_converged = []



    def set_obstacles(self, obstacles:List[Tuple[int, int]]):
        """
        The function `set_obstacles` sets the obstacles for a given object using a list of tuples
        representing coordinates.
        """
        self.obstacles = np.array(obstacles)

        for r, c in obstacles:
            self.obstaclemap[r, c] = 1



    def getReward(self, s:Tuple[int, int, int], action = int):
        """
        The function `getReward` calculates the reward based on the current state `s`, the goal state,
        and obstacles in a grid environment.
        """
        r = -1
        if self.target_state_repr.isgoal(s):
            r += 100

        if action != 0:
            r += -4.55

        if self.obstaclemap[s[0], s[1]]:
            r += -100

        return r

    def isdone(self):
        """
        The function `isdone` checks if the current position (`c_r`, `c_c`) matches the goal position.
        """
        if self.target_state_repr.isdone(self.getState()):
            return True
        return False

    def step(self, a):
        """
        The function `step` updates the position and orientation of an agent based on the action taken
        and returns the state, action, reward, and next state.
        """
        s = self.getPose()
        old_state = self.getState()
        s_prime = self.transition_model.step(s, a)

        if not self.__isingrid((s_prime[0], s_prime[1])):
            s_prime = s

        r = self.getReward(s_prime, a)

        if r < -20: # teste
            s_prime = s

        self.__update_pose(s_prime)
        new_state = self.getState()


        return old_state, a, r, new_state

    def getState(self) -> Tuple[int, int, int]:
        """
        The function `getState` returns a NumPy array containing the values of `c_r`, `c_c`, and
        `c_psi`.
        """
        return self.target_state_repr.pose2state(self.getPose())

    def getPose(self):
        """
        The function `getPose` returns the current pose of an agent in the grid environment.
        """
        return (self.c_r, self.c_c, self.c_psi)

    def reset(self):
        """
        The function `reset` resets the values of `c_r`, `c_c`, and `c_psi` to zero
        """
        self.c_r = 0
        self.c_c = 0
        self.c_psi = 0
        self.target_state_repr.reset()

    def exploring_starts(self):
        """
        The function `exploring_starts` randomly initializes the attributes `c_r`, `c_c`, and `c_psi`
        within specified ranges.
        """
        self.c_r = np.random.randint(self.nrow)
        self.c_c = np.random.randint(self.ncol)
        self.c_psi = np.random.randint(self.n_psi)

        while (self.c_r, self.c_c) in self.obstacles:
            self.c_r = np.random.randint(self.nrow)
            self.c_c = np.random.randint(self.ncol)

        self.target_state_repr.reset()
        #self.target_state_repr.isgoal(self.getPose())

    def exploring_non_converged(self):
        idx = np.random.randint(len(self.non_converged))
        state = self.non_converged[idx]
        self.c_r = state[0]
        self.c_c = state[1]
        self.c_psi = state[2]
        self.target_state_repr.reset()
        self.target_state_repr.set_state(state)
        #self.target_state_repr.isgoal(self.getPose())

    def set_non_converged(self, states:List[Tuple[int, int, int, int]]):
        self.non_converged = states


    def __isingrid(self, position:Tuple[int, int]) -> bool:
        """
        The function `__isingrid` checks if a given position is within the grid.
        """
        row, col = position
        return (row >= 0) and (col >= 0) and (row < self.nrow) and (col < self.ncol)


    def __update_pose(self, pose:Tuple[int, int, int]):
        """
        The function `__update_pose` updates the current pose of the agent.
        """
        self.c_r, self.c_c, self.c_psi = pose


