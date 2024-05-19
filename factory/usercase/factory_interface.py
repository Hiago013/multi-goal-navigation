from abc import ABC, abstractmethod

class factory_interface(ABC):
    @abstractmethod
    def create(self):
        pass