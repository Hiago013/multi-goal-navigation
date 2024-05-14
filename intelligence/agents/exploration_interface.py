from abc import ABC, abstractmethod

class exploration_interface(ABC):
    @abstractmethod
    def choose_action(self, states, qtable):
        pass