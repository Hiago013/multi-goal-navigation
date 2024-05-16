from abc import ABC, abstractmethod
class shorterst_path_interface(ABC):
    @abstractmethod
    def run(self, graph, initial_node, target):
        pass