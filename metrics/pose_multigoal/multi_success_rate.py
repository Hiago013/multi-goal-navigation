from .multi_metrics_interface import multi_metrics_interface
from environment.src import transition_orientation, load_obstacles
from target_state import multi_target
from typing import Tuple, List
from ..generate_combinations import generate_combinations
import numpy as np

# This class likely implements a success rate metric and inherits from a metrics interface.
class multi_success_rate(multi_metrics_interface):
    @staticmethod
    def run(qtable : np.ndarray,
            target_state : multi_target,
            trans_model : transition_orientation) -> Tuple[float, float]:

        available = 0
        count = 0 # conta qnts estados convergem
        shape = qtable.shape[:-1]
        non_converged = []
        visit = np.zeros(shape)
        obstacles = set(load_obstacles().load('environment/maps/map.txt'))

        untarget = [1 for _ in range(len(shape[3:]))]
        pose = list([shape[0], shape[1], shape[2]])

        # Example usage
        combinations = generate_combinations.generate_combinations(shape)#pose + untarget)

        for state in combinations:
            if visit[state] == 1:
                count += 1
                continue
            elif visit[state] == -1:
                continue

            if state[0:2] in obstacles:
                continue

            if np.all(state[3:]):
                continue

            available += 1
            done = False
            max_step = 100

            next_state = state
            next_pose = (next_state[0], next_state[1], next_state[2])

            state_list  = [state]
            while not(target_state.isdone(next_pose)) and max_step > 0:
                best_action = np.argmax(qtable[next_state])
                next_pose = trans_model.step(next_pose, best_action)
                _ = target_state.isgoal(next_pose)
                next_state = target_state.pose2state(next_pose)
                max_step -= 1

                if not multi_success_rate.onmap(next_pose[0], next_pose[1], shape):
                    break

                done = target_state.isdone(next_pose)

                if (next_pose[0], next_pose[1]) in obstacles:
                    break
            target_state.reset()
            if done:
                count += 1
                for step in state_list:
                    visit[step] = 1
            else:
                for step in state_list:
                    non_converged.append(step)
                    visit[step] = -1

        return 100*count/available, non_converged

    @staticmethod
    def onmap(row, col, shape):
        if row < 0 or col < 0:
            return False
        if row >= shape[0] or col >= shape[1]:
            return False
        return True



