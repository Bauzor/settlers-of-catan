class RoadBuilding:
    # An edge index begins at 0 and ends at 5 starting from the top left corner
    def use(game, colour, hex_row, hex_col, edge_index1, edge_index2):
        game.board[hex_row][hex_col][edge_index1].build(colour)
        game.board[hex_row][hex_col][edge_index2].build(colour)

class YearofPlenty:
    def use(game, resource1, resource2):

class Monopoly:
    def use():

class Knight:
    def use():
        