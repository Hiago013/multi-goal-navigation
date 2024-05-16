from abc import ABC, abstractmethod
from typing import Tuple


class target_interface(ABC):
    
    @abstractmethod
    def isdone(self):
        pass