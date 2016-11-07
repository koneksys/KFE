
"""
The tensor rank N has a very simple meaning. It is simply
the number of directions involved in measuring the property."""

from enum import Enum


class Tensor(Enum):
    pass



class Spaceelement(Enum):
    point = 0
    line = 1
    surface = 2
    volume = 3

class Physics(Enum):
    force = 1
    energy = 2
    flux = 3

class Configurationvar(Enum):
    displacement = 1



