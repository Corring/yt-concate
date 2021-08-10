from abc import ABC
from abc import abstractmethod


class Step(ABC):
    def __init__(self):
        pass

    # with @abstructmethod
    # inhereient must have this method
    # input 在这里做字典的用处
    @abstractmethod
    def process(self, data, inputs):
        pass


# 捕捉except的method
# Exception is buit-in
class StepException(Exception):
    pass
