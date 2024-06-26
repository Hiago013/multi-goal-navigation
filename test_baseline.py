from baseline import graph_2d
from environment import transition_position, load_obstacles, path_view
from baseline import dijkstra_search
from baseline import astar_search
from baseline import bfs_search
from baseline.shortest_path_context import shortest_path_context
import numpy as np
from metrics_baseline import metrics_baseline as mbl
import pandas as pd

from time import time
n_row = 16
n_col = 10


target_set = set([(3, 2), (5, 8), (8, 2), (12, 5)]) #set([(3, 2), (1, 6), (9, 7), (11, 4)])#

data_header = ['Planning time', 'Path length', 'Curves', 'Success rate']
data_deploy = []

obstacles = load_obstacles().load('environment/maps/map.txt')
dicti = graph_2d(nrow = 16,
                 ncol = 10,
                 model = transition_position,
                 actions = [0, 1, 2, 3],
                 obstacles = obstacles)

graph = dicti.get_graph()
strategy = dijkstra_search()
path_finder = shortest_path_context(strategy)


for r in range(n_row):
    for c in range(n_col):
        if (r,c) not in obstacles:
            target_set = set([(3, 2), (5, 8), (8, 2), (12, 5)])#set([(6, 2), (14, 3), (4, 5), (12, 7)])
            start_position = (r, c)
            final_path = [start_position]
            init = time()
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
            fim = time()
            distance, curves = mbl.run(final_path)
            planning_time = (fim-init)*1000
            data_deploy.append((planning_time, distance, curves, 100))

for item in final_path:
    print(item[0], item[1])

#pd.DataFrame(data_deploy, columns=data_header).to_excel('data_dijkstra.xlsx')

grid_instance = path_view(16, 10, states=final_path)
grid_instance.run()
