from abc import ABC, abstractmethod
from typing import Tuple

class model_trasition_interface(ABC):
    @abstractmethod
    def step(state , action):
        pass