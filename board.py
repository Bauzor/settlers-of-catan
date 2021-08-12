from tiles import Hex, Vertex
from enumerations import Colour, Resource, Piece, Difficulty
from beginner_board_constants import BoardConfigurations

class Board(BoardConfigurations):

    def __init__(self, level):
        if (level == Difficulty.BEGINNER):

            beginner_resource_order = self.beginner_resource_order
            beginner_num_tokens_order = self.beginner_num_tokens_order

            board = [
                [],
                [],
                [],
                [],
                []
            ]

            # Hex Generation using Configuration
            # Handles sharing of vertices
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

            # Sets all ports
            board[0][0].vertices[0].setPort(Resource.NONE)
            board[0][0].vertices[0].setPort(Resource.NONE)
            board[0][1].vertices[1].setPort(Resource.WOOL)
            board[0][1].vertices[2].setPort(Resource.WOOL)
            board[1][0].vertices[0].setPort(Resource.ORE)
            board[1][0].vertices[5].setPort(Resource.ORE)
            board[1][3].vertices[1].setPort(Resource.NONE)
            board[1][3].vertices[2].setPort(Resource.NONE)
            board[2][4].vertices[2].setPort(Resource.NONE)
            board[2][4].vertices[3].setPort(Resource.NONE)
            board[3][0].vertices[0].setPort(Resource.GRAIN)
            board[3][0].vertices[5].setPort(Resource.GRAIN)
            board[3][3].vertices[3].setPort(Resource.BRICK)
            board[3][3].vertices[4].setPort(Resource.BRICK)
            board[4][0].vertices[4].setPort(Resource.NONE)
            board[4][0].vertices[5].setPort(Resource.NONE)
            board[4][1].vertices[3].setPort(Resource.LUMBER)
            board[4][1].vertices[4].setPort(Resource.LUMBER)

            # Set all adjacencies of vertices
            for row_index, row in enumerate(board):
                for column_index, hex_ in enumerate(row):
                    for position, vertex in enumerate(hex_.vertices):
                        if not bool(vertex.adjacent):

                            vertex.setNeighbor(hex_.vertices[(position + 1) % 6])
                            vertex.setNeighbor(hex_.vertices[(position - 1) % 6])

                            if position == 0:
                                if (row_index not in [0, 1, 2]) or not (column_index == 0):
                                    if column_index == 0:
                                        vertex.setNeighbor(board[row_index - 1][column_index].vertices[5])
                                    else:
                                        vertex.setNeighbor(row[column_index - 1].vertices[1])

                            elif position == 1:
                                if row_index != 0:
                                    if (row_index in [1, 2] and column_index == 0):
                                        vertex.setNeighbor(board[row_index - 1][column_index].vertices[0])
                                    elif (row_index in [1, 2]):
                                        vertex.setNeighbor(board[row_index - 1][column_index - 1].vertices[2])
                                    else:
                                        vertex.setNeighbor(board[row_index - 1][column_index].vertices[2])

                            elif position == 2:
                                if row_index not in [0, 1, 2] or not (column_index == (len(row) - 1)):

                                    if column_index == (len(row) - 1):
                                        vertex.setNeighbor(board[row_index - 1][column_index + 1].vertices[3])
                                    else:
                                        vertex.setNeighbor(row[column_index + 1].vertices[1])

                            elif position == 3:
                                if row_index not in [2, 3, 4] or not (column_index == (len(row) - 1)):
                                    if column_index == (len(row) - 1):
                                        vertex.setNeighbor(board[row_index + 1][column_index + 1].vertices[2])
                                    else:
                                        vertex.setNeighbor(row[column_index + 1].vertices[4])
                            elif position == 4:
                                if row_index != 4:
                                    if (row_index in [2, 3] and column_index == 0):
                                        vertex.setNeighbor(board[row_index + 1][column_index].vertices[5])
                                    elif (row_index in [2, 3]):
                                        vertex.setNeighbor(board[row_index + 1][column_index - 1].vertices[3])
                                    else:
                                        vertex.setNeighbor(board[row_index + 1][column_index].vertices[3])

                            elif position == 5:
                                if row_index not in [2, 3, 4] or not (column_index == 0):
                                    if column_index == 0:
                                        vertex.setNeighbor(board[row_index + 1][column_index].vertices[0])
                                    else:
                                        vertex.setNeighbor(row[column_index - 1].vertices[4])

            self.board = board

    # Obtain a hex at given board coordinates and return None if there is no hex at the specified coordinate
    def getHex(self, hex_row, hex_col):
        map = {
            0:3,
            1:4,
            2:5,
            3:4,
            4:3,
        }
        if (hex_row in range(5) and hex_col in range(map[hex_row])):
            return self.board[hex_row][hex_col]
        else:
            return None

    def build(self, piece, colour, hex_row, hex_col, index1, index2=None):
        """
        Build handles the creation of roads/cities/settlements
        Does not handle
        - if player has enough roads/cities/settlements
        - payment of the resources
        """
        map = {
            0:3,
            1:4,
            2:5,
            3:4,
            4:3,
        }
        # Input verification
        assert(index1 in range(6))
        assert(index2 in range(6))
        assert(piece in Piece)
        assert(colour in Colour)
        assert(hex_row in range(5))
        assert(hex_col in range(map[hex_row]))

        # Set the current hex
        curr_hex = self.getHex(hex_row, hex_col)

        # Building a road
        if (piece == Piece.ROAD):
            # Set the counter clockwise and clockwise indices
            ccw_index = min(index1, index2) if index1 in range(5) else 5
            cw_index = max(index1, index2) if ccw_index != 5 else 0
            # Get all Neighbors of respective indices
            ccw_adjacent_vertices = curr_hex.vertices[ccw_index].adjacent
            cw_adjacent_vertices = curr_hex.vertices[cw_index].adjacent
            # Generate boolean values for build conditions
            edge_colour_is_none = ccw_adjacent_vertices.values()[0].colour == Colour.NONE
            has_neighbouring_settlement = colour in [
                curr_hex.vertices[ccw_index].getColour(),
                curr_hex.vertices[cw_index].getColour(),
            ]
            has_unblocked_neighbouring_road_ccw = curr_hex.vertices[ccw_index].getColour() == Colour.NONE and colour in [
                ccw_adjacent_vertices.values()[1],
                ccw_adjacent_vertices.values()[2],
            ]
            has_unblocked_neighbouring_road_cw = curr_hex.vertices[cw_index].getColour() == Colour.NONE and colour in [
                cw_adjacent_vertices.values()[1],
                cw_adjacent_vertices.values()[2],
            ]
            has_unblocked_neighbouring_road = has_unblocked_neighbouring_road_ccw and has_unblocked_neighbouring_road_cw
            assert(edge_colour_is_none and (has_neighbouring_settlement or has_unblocked_neighbouring_road))
            curr_hex.setICP(ccw_index, colour, Piece.ROAD, cw_index)

        # Building a settlement
        elif (piece == Piece.SETTLEMENT):
            # Validate all neighbouring vertices do not have a settlement
            # and at least one neighbouring edge is of the same colour
            has_road = False
            for neighbouring_vertex, neighbouring_edge in curr_hex.vertices[index1].adjacent.items():
                assert(Colour.NONE == neighbouring_vertex.getColour())
                if neighbouring_edge == colour:
                    has_road = True
            if has_road:
                curr_hex.setICP(index1, colour, piece)

        else:
            # Validate there is a preexisting settlement where the city is being built
            has_settlement = curr_hex.vertices[index1].getPiece() == Piece.SETTLEMENT
            is_same_colour = curr_hex.vertices[index1].getColour() == colour
            if (is_same_colour and has_settlement):
                curr_hex.setICP(index1, colour, piece)
