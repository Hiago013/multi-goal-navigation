from abc import ABC, abstractmethod

class gridworld_interface(ABC):
    @abstractmethod
    def step(self, state:tuple, action:int):
        pass
    @abstractmethod
    def isdone(self, state:tuple):
        pass
    @abstractmethod
    def reset(self):
        pass
    @abstractmethod
    def getReward(self, state:tuple):
        pass