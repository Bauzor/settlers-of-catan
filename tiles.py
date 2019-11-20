from enumerations import Colour, Resource, Piece

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
        '''
        self.colour = Colour.NONE
        self.port = Resource.NONE
        self.piece = Piece.NONE
        self.adjacent = {}
    
    def getColour(self):
        return self.colour
    
    def getPiece(self):
        return self.piece
    
    def setNeighbor(self, neighbor, colour=Colour.NONE):
        self.adjacent[neighbor] = colour

    def setPieceAndColour(self, piece, colour):
        self.piece = piece
        self.colour = colour
    

class Hex:
    '''
    Hexes own a list of Vertices and Edges which hold vertex and edge properties
    '''
    def __init__(
        self,
        value = None,
        resource = Resource.NONE,
        vertices = [],
        robber = False
    ):
        self.value = value
        self.resource = resource
        self.vertices = vertices
        self.robber = robber

    def getResource(self):
        '''
        Returns: Enum class Resource
        '''
        return self.resource

    def getRobber(self):
        '''
        Returns: bool
            boolean of if robber is on hex
        '''
        return self.robber

    def setRobber(self, value):
        '''
        Args:
            value: bool
        Side - Effects:
            mutates robber to be value
        '''
        self.robber = value
    

    def setICP(self, index1, colour=Colour.NONE, piece=Piece.NONE, index2=None):
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
            self.vertices[index1].setNeighbor(self.verices[index2], colour)
            self.vertices[index2].setNeighbor(self.vertices[index1], colour)
        else:
            self.vertices[index1].setPieceAndColour(piece, colour)