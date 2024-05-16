from typing import Dict, Tuple, List, Optional
from ..data_structure import Queue
from ..shorterst_path_interface import shorterst_path_interface

class bfs_search(shorterst_path_interface):
    def run(self,   graph:Dict[Tuple[int, int], Dict[Tuple[int, int], float]],
                    start: Tuple,
                    target: Tuple) -> List[Tuple[int, int]]:

        frontier = Queue()
        frontier.put(start)
        came_from = dict()
        came_from[start] = None

        while not frontier.empty():
            current = frontier.get()

            if current == target: # early exit
                break

            for next in graph[current]:
                if next not in came_from:
                    frontier.put(next)
                    came_from[next] = current
        path = self.__reconstruct_path(came_from, start, target)
        return path

    def __reconstruct_path(self, came_from:dict,
                            start:Tuple, goal:Tuple) -> List[Tuple[int, int]]:

        current = goal
        path = []
        if goal not in came_from: # no path was found
            return []
        while current != start:
            path.append(current)
            current = came_from[current]
        path.append(start) # optional
        path.reverse() # optional
        return path