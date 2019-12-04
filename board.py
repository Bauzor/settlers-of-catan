from tiles import Hex, Vertex
from enumerations import Colour, Resource, Piece
from logs.base import BaseHelpers

class Board(BaseHelpers):

    def __init__(self, level, **kwags):
        super().__init__(**kwags)
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
                self.log.info(f"Row Index: {row_index}")
                for column_index, hex_ in enumerate(row):
                    self.log.info(f"Column Index: {column_index}")
                    for position, vertex in enumerate(hex_.vertices):
                        self.log.info(f"Vertex Index {position}")
                        if not bool(vertex.adjacent):
                            self.log.info(f"Adjacencies not set yet, setting adjacencies...")

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
                                    self.log.info(f"Vertex has a third Neighbour")
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
        if (hex_row in range(5) and hex_col in range(map[hex_row]))
            return self.board[hex_row][hex_col]
        else:
            return None

    def build(self, piece, colour, hex_row, hex_col, index1, index2):
        """
        Build handles the creation of roads/cities/settlements
        Does not handle
        - if player has enough roads/cities/settlements
        - payment of the resources
        """

        # Building a road
        if (piece == "road"):
            