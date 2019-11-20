from .tiles import Hex, Edge, Vertex

class Board():

    def __init__(level):

        if (level == "Beginner"):

            beginner_resource_order = [
                [Resource.LUMBER, Resource.WOOL, Resource.GRAIN],
                [Resource.BRICK, Resource.ORE, Resource.BRICK, Resource.GRAIN],
                [Resource.NONE, Resource.LUMBER, Resource.GRAIN, Resource.LUMBER, Resource.GRAIN],
                [Resource.BRICK, Resource.WOOL, Resource.WOOL, Resource.ORE],
                [Resource.ORE, Resource.GRAIN, Resource.LUMBER]
            ]

            beginner_num_tokens_order = [
                [11, 12, 9],
                [4, 6, 5, 10],
                [None, 3, 11, 4, 8],
                [8, 10, 9, 3],
                [5, 2, 6],
            ]

            board = [
                [],
                [],
                [],
                [],
                []
            ]

            for row, (resource_row, num_token_row) in enumerate(zip(beginner_resource_order, beginner_num_tokens_order)):
                for column, (resource, value) in enumerate(zip(resource_row, num_token_row)):
                    if (row == 0 and column == 0):
                        board[row].append(
                            Hex(value, resource, [Vertex() for _ in range(6)])
                        )
                    elif (row == 0 and column != 0):
                        board[row].append(
                            Hex(value, resource, [board[row][column-1].vertices[2]] + [Vertex() for _ in range(4)] + [board[row][column-1].vertices[3]])
                        )
                    elif (row == 1 or row == 2):
                        if (column == 0):
                            board[row].append(
                                Hex(value, resource, [Vertex(), board[row-1][column].vertices[4], board[row-1][column].vertices[5]] + [Vertex() for _ in range(3)])
                            )
                        elif (column == 1 or column == 2) or (row == 2 and column == 3):
                            board[row].append(
                                Hex(
                                    value,
                                    resource,
                                    [
                                        board[row][column-1].vertices[2],
                                        board[row-1][column].vertices[5],
                                        board[row-1][column].vertices[4],
                                        Vertex(),
                                        Vertex(),
                                        board[row][column-1].vertices[3],
                                    ]
                                )
                            )
                        else:
                            board[row].append(
                                Hex(value, resource, [board[row-1][column-1].vertices[4], board[row-1][column-1].vertices[3]] + [Vertex() for _ in range(3)] + [board[row][column-1].vertices[3]])
                            )
                    else:
                        if (column == 0):
                            board[row].append(
                                Hex(value, resource, [board[row-1][column].vertices[4], board[row-1][column].vertices[3], board[row-1][column+1].vertices[4]] + [Vertex() for _ in range(3)])
                            )
                        else:
                            board[row].append(
                                Hex(
                                    value,
                                    resource,
                                    [
                                        board[row][column-1].vertices[2],
                                        board[row-1][column+1].vertices[5],
                                        board[row-1][column+1].vertices[4],
                                        Vertex(),
                                        Vertex(),
                                        board[row][column-1].vertices[3],
                                    ]
                                )
                            )
            self.board = board


    # Obtain a hex at given board coordinates and return None if there is no hex at the specified coordinate
    def getHex(self, hex_row, hex_col):
        try:
            return self.board[hex_row][hex_col]
        except:
            return None
    
    # Given a hex from the board, return all it's neighbours in a list starting from the top left and going clockwise
    def hexNeighbours(self, hex_row, hex_col):
        if ( hex_row == 0 and hex_row == 1 ):

            zeroth_hex = self.board.getHex(hex_row - 1, hex_col - 1)
            first_hex = self.board.getHex(hex_row - 1, hex_col)

            third_hex = self.board.getHex(hex_row + 1, hex_col + 1)
            fourth_hex = self.board.getHex(hex_row + 1, hex_col)

        elif ( hex_row == 2 ):

            zeroth_hex = self.board.getHex(hex_row - 1, hex_col - 1)
            first_hex = self.board.getHex(hex_row - 1, hex_col)
            
            third_hex = self.board.getHex(hex_row + 1, hex_col)
            fourth_hex = self.board.getHex(hex_row + 1, hex_col - 1)
            
        elif ( hex_row == 3 or hex_row == 4 ):

            zeroth_hex = self.board.getHex(hex_row - 1, hex_col)
            first_hex = self.board.getHex(hex_row - 1, hex_col + 1)
            
            third_hex = self.board.getHex(hex_row + 1, hex_col)
            fourth_hex = self.board.getHex(hex_row + 1, hex_col - 1)

        second_hex = self.board.getHex(hex_row, hex_col + 1)
        fifth_hex = self.board.getHex(hex_row, hex_col - 1)
        return [zeroth_hex, first_hex, third_hex, fourth_hex, fifth_hex]

    def build(self, piece, colour, hex_row, hex_col, index):
        """
        Build handles the creation of roads/cities/settlements
        Does not handle
        - if player has enough roads/cities/settlements
        - payment of the resources
        """

        # Building a road
        if (piece == "road"):

            # check is already on current edge
            if ( !( self.board[hex_row][hex_col].edges[index].isFree() ) ):
                raise "There is already a road here"

            # check if colour does not have settlement/city on neighbouring vertices
            if (( self.board[hex_row][hex_col].vertices[index].getColour() != colour ) or
                ( self.board[hex_row][hex_col].vertices[(index + 1) % 6].getColour() != colour )):

                # if the other hex sharing this edge does not exist
                if (self.board.hexNeighbours(hex_row, hex_col)[index] != None):

                    # check if neighbour vertex in counter - clockwise direction has no settlement/city AND
                    # the neighbouring edges to that vertex have a road of the same colour
                    if (( self.board[hex_row][hex_col].vertices[index].getColour() == None) and 
                        (( self.hexNeighbours(hex_row, hex_col)[index].edges[(index + 2) % 6].getColour == colour ) or
                        ( self.board[hex_row][hex_col][(index + 1) % 6].getColour() == colour ))):
                        self.board[hex_row][hex_col].edges[index].build(colour)

                    # check if neighbour vertex in clockwise direction has no settlement/city
                    # check if neighbouring edges to that vertex have a road of the same colour 
                    elif (( self.board[hex_row][hex_col].vertices[(index + 1) % 6].getColour() == None) and
                        (( self.board.hexNeighbours(hex_row, hex_col)[index].edges[(index + 4) % 6].getColour() == colour ) or
                        ( self.board[hex_row][hex_col].edges[(index - 1) % 6].getColour == colour ))):
                        self.board[hex_row][hex_col].edges[index].build(colour)
                
                # the neighbouring hex does not exist        
                else:

                    # No settlement exists on vertex in clockwise direction AND
                    # the neighbouring edge in the clockwise direciton is the same colour
                    if (( self.board[hex_row][hex_col].vertices[index].getColour() == None ) and
                        ( self.board[hex_row][hex_col][(index + 1) % 6].getColour() == colour )):
                        self.board[hex_row][hex_col].edges[index].build(colour)

                    # No settlement exists on vertex in counter - clockwise direction AND
                    # the neighbouring edge in the counter - clockwise direciton is the same colour
                    elif (( self.board[hex_row][hex_col].vertices[(index + 1) % 6].getColour() == None) and
                        ( self.board[hex_row][hex_col].edges[(index - 1) % 6].getColour == colour )):
                        self.board[hex_row][hex_col].edges[index].build(colour)

            # has a settlement/city on neighbour vertices to the edge
            else:
                self.board[hex_row][hex_col].edges[index].build(colour)

        # Building a settlement or city
        elif ( piece == "settlement" or piece == "city" ):

            # check that nothing is built on the current vertex
            if ( !( self.board[hex_row][hex_col].vertices[index].isFree() ) ):
                raise "There is already a {} here".format( self.board[hex_row][hex_col].vertices[index].getBuildType() )

            # check that at least one neighbouring edge is the same colour
            if (( self.board[hex_row][hex_col].edges[index].getColour() == colour ) or 
                ( self.board[hex_row][hex_col].edges[(index - 1) % 6].getColour() == colour)):
                
                # check whether or not there is a third edge
                if ((  ))
            
            # check that no neighbouring vertex has a settlement/city

        else:
            raise "The piece provided is not a valid piece"