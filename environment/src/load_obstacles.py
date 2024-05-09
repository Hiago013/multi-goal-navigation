from typing import List, Tuple
class load_obstacles():
    def load(self, path : str = '') -> List[Tuple[int, int]]:
        obstacles = []
        with open(path, 'r') as f:
                # Use a for loop to write each line of data to the file
                line = f.readline()
                while line != '':
                    obstacles.append(tuple(map(int, line.split())))
                    line = f.readline()
        return obstacles