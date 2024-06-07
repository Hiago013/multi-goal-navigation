from baseline import graph_2d
from environment import transition_position, load_obstacles, path_view
from baseline import dijkstra_search
from baseline import astar_search
from baseline import bfs_search
from baseline.shortest_path_context import shortest_path_context
import numpy as np
from metrics_baseline import metrics_baseline as mbl
target_set = set([(3, 2), (5, 8), (8, 2), (12, 5)])
start_position = (15, 9)

obstacles = load_obstacles().load('environment/maps/map.txt')
dicti = graph_2d(nrow = 16,
                 ncol = 10,
                 model = transition_position,
                 actions = [0, 1, 2, 3],
                 obstacles = obstacles)

graph = dicti.get_graph()
strategy = dijkstra_search()
path_finder = shortest_path_context(strategy)

final_path = [start_position]


while len(target_set) > 0:
    distances = list(map(lambda X: np.sqrt((X[0] - start_position[0])**2 + (X[1] - start_position[1])**2), target_set))
    argmin_dist = np.argmin(distances)
    target = list(target_set)[argmin_dist]
    target_set.remove(target)
    path = path_finder.find_shortest_path(graph, start_position, target)
    start_position = target
    final_path += path[1:] # remove the first element of the
    for item in target_set:
        if item in path:
            target_set.remove(item)
print(final_path)

print(mbl.run(final_path))

grid_instance = path_view(16, 10, states=final_path)
grid_instance.run()
