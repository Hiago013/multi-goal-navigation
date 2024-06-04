from typing import List, Tuple
import numpy as np

class metrics_baseline:
    @staticmethod
    def run(path:List[Tuple[int, int]]):
        path_length = len(path)

        n_turns = 0

        for idx_path in range(2, len(path)):
            crr = np.array(path[idx_path])
            prev = np.array(path[idx_path-1])
            prev_v = np.array(path[idx_path-2])

            crr_dif = crr - prev
            prev_dif = prev - prev_v

            if np.all( (crr_dif + prev_dif) == (0, 0)):
                n_turns += 2

            if not np.any(crr_dif == prev_dif):
                n_turns += 1

        return path_length, n_turns