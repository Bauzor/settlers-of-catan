from enum import (
    auto,
    Enum,
    IntEnum
)

class Colour(Enum):
    NONE = auto()
    RED = auto()
    BLUE = auto()
    WHITE = auto()
    ORANGE = auto()
    GREEN = auto()
    BROWN = auto()

class Resource(Enum):
    NONE = auto()
    BRICK = auto()
    WOOL = auto()
    ORE = auto()
    GRAIN = auto()
    LUMBER = auto()

class Piece(Enum):
    NONE = auto()
    ROAD = auto()
    SETTLEMENT = auto()
    CITY = auto()

class DiceValues(IntEnum):
    NONE = None
    I = 1
    II = 2
    III = 3
    IV = 4
    V = 5
    VI = 6

class Difficulty(Enum):
    BEGINNER = auto()
