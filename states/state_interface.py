from abc import ABC, abstractmethod

class state_interface(ABC):
    @abstractmethod
    def getState(self):
        pass

    @abstractmethod
    def setState(self, s):
        pass

    @abstractmethod
    def getShape(self):
        pass
