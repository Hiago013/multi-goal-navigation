from typing import List, Tuple
class load_obstacles():
    def load(self, path : str = '') -> List[Tuple[int, int]]:
        """
        This Python function loads obstacle data from a file and returns it as a list of tuples
        containing integer values.
        """
        obstacles = []
        with open(path, 'r') as f:
                line = f.readline()
                while line != '':
                    obstacles.append(tuple(map(int, line.split())))
                    line = f.readline()
        return obstacles