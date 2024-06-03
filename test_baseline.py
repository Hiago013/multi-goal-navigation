from baseline import graph_2d
from environment import transition_position, load_obstacles
from baseline import dijkstra_search
from baseline import astar_search
from baseline import bfs_search
from baseline.shortest_path_context import shortest_path_context
import numpy as np

target_set = set([(6, 2), (4, 5), (14, 3), (12, 7)])
verifier = [0 for _ in range(len(target_set))]
look_up_target = np.array(list(target_set))
lookup_target_check = dict(zip(target_set, verifier))
start_position = (0, 0)


obstacles = load_obstacles().load('environment/maps/map.txt')
dicti = graph_2d(nrow=16, ncol=10, model=transition_position, actions = [0, 1, 2, 3], obstacles = obstacles)
graph = dicti.get_graph()
strategy = astar_search()
path_finder = shortest_path_context(strategy)

distances = list(map(lambda X: np.sqrt((X[0] - start_position[0])**2 + (X[1] - start_position[1])**2), target_set))
argmin_dist = np.argmin(distances)

path = path_finder.find_shortest_path(graph, (0, 0), (12, 7))

print(path)
