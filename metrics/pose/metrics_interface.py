from abc import ABC, abstractmethod
from typing import Tuple
class metrics_interface(ABC):
    @abstractmethod
    def run(self, qtable, state : Tuple[int, int, int]):
        return None
