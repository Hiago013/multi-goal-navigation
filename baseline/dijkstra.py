from .shorterst_path_interface import shorterst_path_interface
from typing import Dict, Tuple, List

class dijkstra(shorterst_path_interface):
    def __invert_path(self, path:list):
        return path[::-1]
    
    def run(self,   graph:Dict[Tuple[int, int], Dict[Tuple[int, int], float]],
                    initial_node: Tuple,
                    target : Tuple) -> List[Tuple[int, int]]:
        distances = {}
        parents = {}
        best_path = []
        for node in graph:
            distances[node] = float('inf')
            parents[node] = None
        distances[initial_node] = 0
        queue = [initial_node]
        while queue:
            current = queue.pop(0)
            for neighbor in graph[current]:
                if distances[neighbor] == float('inf'):
                    distances[neighbor] = distances[current] + graph[current][neighbor]
                    parents[neighbor] = current
                    queue.append(neighbor)
        current = target
        while parents[current] is not None:
            best_path.append(current)
            current = parents[current]
        best_path.append(current)
        return self.__invert_path(best_path)
