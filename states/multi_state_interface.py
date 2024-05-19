from abc import ABC, abstractmethod

class multi_state_interface(ABC):
    @abstractmethod
    def getState(self):
        pass

    @abstractmethod
    def setState(self, s):
        pass

    @abstractmethod
    def getShape(self):
        pass
    
    @abstractmethod
    def getTargets(self):
        pass
    
    @abstractmethod
    def reset(self):
        pass