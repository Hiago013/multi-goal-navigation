from .strategies import dijkstra_search

class shortest_path_context:
    def __init__(self, strategy : dijkstra_search):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def find_shortest_path(self, graph, initial_node, target):
        return self.strategy.run(graph, initial_node, target)