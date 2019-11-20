from enum import Enum, auto

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