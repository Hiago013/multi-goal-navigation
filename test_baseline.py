from intelligence import qlearning, success_rate, all_metrics, egreedy_decay
from environment import gridworld, load_obstacles, goal_position, goal_orientation
from environment import transition_orientation as trans_model
from baseline import graph_2d
from environment import transition_position
import numpy as np
import matplotlib.pyplot as plt
from baseline import dijkstra_search
from baseline import astar_search
from baseline import bfs_search
from baseline.shortest_path_context import shortest_path_context

dicti = graph_2d(nrow=5, ncol=5, model=transition_position, actions=[0, 1, 2, 3])
graph = dicti.get_graph()
strategy = astar_search()
path_finder = shortest_path_context(strategy)
path = path_finder.find_shortest_path(graph, (3,3), (0,0))

print(path)
