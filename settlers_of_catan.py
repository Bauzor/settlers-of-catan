import random
import beginner_board
from hex import hex
from player import player

#-------------
#for the advanced board
#-------------
#values that can be rolled (list is used to help generate the hex values)
tokens = [2,3,3,4,4,5,5,6,6,8,8,9,9,10,10,11,11,12]
#possible resources that can be popped to be put into hex resource types
resources = [
    "desert",
    "brick",
    "brick",
    "brick",
    "ore",
    "ore",
    "ore",
    "wool",
    "wool",
    "wool",
    "wool",
    "grain",
    "grain",
    "grain",
    "grain",
    "lumber",
    "lumber",
    "lumber",
    "lumber"
]
#Types of Maritime Trades
maritime = [
    "generic","generic","generic","generic",
    "brick",
    "wool",
    "ore",
    "grain",
    "lumber"]
