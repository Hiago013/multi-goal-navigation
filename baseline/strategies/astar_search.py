from ..shorterst_path_interface import shorterst_path_interface
from typing import Dict, Tuple, List
from ..data_structure import PriorityQueue

class astar_search(shorterst_path_interface):
    def run(self, graph:Dict[Tuple[int, int], Dict[Tuple[int, int], float]],
                    start: Tuple,
                    target: Tuple) -> List[Tuple[int, int]]:
        frontier = PriorityQueue()
        frontier.put(start, 0)
        came_from = dict()
        cost_so_far = dict()
        came_from[start] = None
        cost_so_far[start] = 0
        while not frontier.empty():
            current = frontier.get()

            if current == target:
                break

            for next in graph[current]:
                new_cost = cost_so_far[current] + graph[current][next]
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost + self.__heuristic(next, target)
                    priority = new_cost
                    frontier.put(next, priority)
                    came_from[next] = current
        path = self.__reconstruct_path(came_from, start, target)
        return path

    def __heuristic(self, a:Tuple, b:Tuple) -> float:
        """
        The function `heuristic()` calculates the euclidean distance between two points.
        """
        return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5

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
