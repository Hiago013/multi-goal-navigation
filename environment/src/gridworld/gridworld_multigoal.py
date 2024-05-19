import numpy as np
from typing import Tuple, List
from states import pose_state, multi_pose_state
from .gridworld_interface import gridworld_interface
from ..targets import multi_goal_position
from ..transition_models import transition_orientation

class gridworld_multigoal(gridworld_interface):
    def __init__(self, nrow, ncol, goal:multi_goal_position,
                 transition_model : transition_orientation,
                 state_repr:multi_pose_state):
        """
        This function initializes variables for a grid environment with a specified number of rows and
        columns, a goal position, and transition matrices for position and orientation.
        """
        self.c_r = 0
        self.c_c = 0
        self.c_psi = 0

        self.visited = dict(zip(state_repr.getTargets(), [0]*state_repr.n_targets))

        self.nrow = nrow
        self.ncol = ncol
        self.n_psi = 4


        self.goal = goal
        self.obstacles = np.array([])
        self.transition_model = transition_model
        self.state_repr : multi_pose_state = state_repr


    def set_obstacles(self, obstacles:List[Tuple[int, int]]):
        """
        The function `set_obstacles` sets the obstacles for a given object using a list of tuples
        representing coordinates.
        """
        self.obstacles = np.array(obstacles)

    def getReward(self, s:Tuple[int, int, int], action = int):
        """
        The function `getReward` calculates the reward based on the current state `s`, the goal state,
        and obstacles in a grid environment.
        """
        r = -1
        if self.goal.isgoal(s):
            r += 100
            self.visited[(s[0], s[1])] = 1

        if action != 0:
            r += -5

        for i in range(len(self.obstacles)):
            if np.all(self.obstacles[i] == s[0:2]):
                r += -50
                break
        return r

    def isdone(self):
        """
        The function `isdone` checks if the current position (`c_r`, `c_c`) matches the goal position.
        """
        if self.goal.isdone(self.getState()):
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


        self.__update_pose(s_prime)
        self.__update_state(s_prime)
        new_state = self.getState()



        return old_state, a, r, new_state

    def getState(self) -> Tuple[int, int, int]:
        """
        The function `getState` returns a NumPy array containing the values of `c_r`, `c_c`, and
        `c_psi`.
        """
        return self.state_repr.getState()

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
        self.visited = dict(zip(self.state_repr.getTargets(), [0]*self.state_repr.n_targets))
        self.goal.reset()
        self.state_repr.reset()
        self.__update_state((self.c_r, self.c_c, self.c_psi))

    def exploring_starts(self):
        """
        The function `exploring_starts` randomly initializes the attributes `c_r`, `c_c`, and `c_psi`
        within specified ranges.
        """
        self.c_r = np.random.randint(self.nrow)
        self.c_c = np.random.randint(self.ncol)
        self.c_psi = np.random.randint(self.n_psi)
        s = (self.c_r, self.c_c, self.c_psi)
        self.visited = dict(zip(self.state_repr.getTargets(), [0]*self.state_repr.n_targets))
        self.goal.reset()
        self.state_repr.reset()
        self.__update_state((self.c_r, self.c_c, self.c_psi))

        if self.goal.isgoal(s):
            self.visited[(s[0], s[1])] = 1

    def __isingrid(self, position:Tuple[int, int]) -> bool:
        """
        The function `__isingrid` checks if a given position is within the grid.
        """
        row, col = position
        return (row >= 0) and (col >= 0) and (row < self.nrow) and (col < self.ncol)

    def __update_state(self, pose):
        """
        The function `__update_state` updates the current pose of the agent.
        """
        state = list(pose) + list(self.visited.values())
        state = tuple(state)
        self.state_repr.setState(state)

    def __update_pose(self, pose:Tuple[int, int, int]):
        """
        The function `__update_pose` updates the current pose of the agent.
        """
        self.c_r, self.c_c, self.c_psi = pose
