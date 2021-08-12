from enumerations import (
    Colour,
    Resource,
    Piece,
    DiceValues
)
from typing import List
import logging

class Vertex:
    '''
    Vertex keeps track of buildings

    '''
    def __init__(self):
        '''
        Args:
            colour: Enum Class Colour
            port: Enum Class Resource
            piece: Enum Class Piece
            adjacent: Vertex : Enum Class Colour
        '''
        self.colour = Colour.NONE
        self.port = Resource.NONE
        self.piece = Piece.NONE
        self.adjacent = {}
        self.logger = logging.getLogger("Vertex")
        self.logger.info('Creating Vertex Instance')
    
    def getColour(self):
        self.logger.info(f"Got Colour: {self.colour}")
        return self.colour
    
    def getPiece(self):
        self.logger.info(f"Got Piece: {self.piece}")
        return self.piece

    def setPort(self, value):
        self.logger.info(f"Port value before setPort is {self.port}")
        self.logger.info(f"Set Port as {value}")
        self.port = value
        self.logger.info(f"Port value after setPort is {self.port}")
    
    def setNeighbor(self, neighbor, colour=Colour.NONE):
        self.logger.info(f"Neighbour list before setNeighbor is {self.adjacent}")
        self.logger.info(f"Set Neighbor as {neighbor} : {colour}")
        self.adjacent[neighbor] = colour
        self.logger.info(f"Neighbour list after setNeighbour is {self.adjacent}")

    def setPieceAndColour(self, piece, colour):
        self.logger.info(f"Piece and colour before setPieceAndColour is {self.piece}, {self.colour}")
        self.logger.info(f"Set Piece as {piece} and Colour as {colour}")
        self.piece = piece
        self.colour = colour
        self.logger.info(f"Piece and colour after setPieceAndColour is {self.piece}, {self.colour}")

class Hex:
    '''
    Hexes own a list of Vertices and Edges which hold vertex and edge properties
    '''
    def __init__(
        self,
        value: int = None,
        resource: Resource = Resource.NONE,
        vertices: List[Vertex] = [],
        robber: bool = False
    ):
        self.value = value
        self.resource = resource
        self.vertices = vertices
        self.robber = robber
        self.logger = logging.getLogger("Hex")
        self.logger.info('Created Hex Instance')

    def getResource(self):
        '''
        Returns: Enum class Resource
        '''
        self.logger.info(f"Got resource: {self.resource}")
        return self.resource

    def hasRobber(self):
        '''
        Returns: bool
            boolean of if robber is on hex
        '''
        self.logger.info(f"Hex has robber is {self.robber}")
        return self.robber

    def setRobber(self, value: bool):
        '''
        Args:
            value: bool
        Side - Effects:
            mutates robber to be value
        '''
        self.logger.info(f"Value before setting robber is {self.robber}")
        self.robber = value
        self.logger.info(f"Value after setting robber is {self.robber}")
    

    def setICP(
        self,
        index1: DiceValues,
        colour: Colour=Colour.NONE,
        piece: Piece=Piece.NONE,
        index2: DiceValues=None):
        '''
        setICP -> set Piece, Colour and Index
        Args:
            index1: int
                - the location of where the coloured piece is built or where road starts
                - [0, 6]
            index2: int
                - location of where the road will finish
            colour: Colour
            piece: Piece
            
        Side - Effects:
            builds the given coloured piece in the index of the current hex
        '''
        if ( piece == Piece.ROAD ):
            self.vertices[index1].setNeighbor(self.vertices[index2], colour)
            self.vertices[index2].setNeighbor(self.vertices[index1], colour)
        else:
            self.vertices[index1].setPieceAndColour(piece, colour)