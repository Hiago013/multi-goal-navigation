from ..targets import multi_goal_position
from ..states import multi_pose_state
from typing import Tuple

class multi_target():
    def __init__(self, target_repr : multi_goal_position,
                       state_repr : multi_pose_state) -> None:
        self.target_repr = target_repr
        self.state_repr = state_repr
        self.__shape = state_repr.getShape()
    
    def isgoal(self, pose: Tuple[int, int, int]) -> bool:
        return self.target_repr.isgoal(pose)
    
    def isdone(self, pose: Tuple[int, int, int]) -> bool:
        return self.target_repr.isdone(pose)
    
    def pose2state(self, pose : Tuple[int, int, int]):
        state = list(pose)
        state.extend(self.target_repr.get_visited_state())
        return tuple(state)
    
    def get_shape(self):
        return self.__shape
    
    def reset(self):
        self.state_repr.reset()
        self.target_repr.reset()
    
    
    