from .player import Player
from .board import Board
import random

class Game:

    # Ordered list of Player objects
    players = []

    # Ordered list of Hex Objects
    board = []

    # Ordered list of Development Cards
    deck = []

    # Resources in the bank
    resources = {
		"brick":0,
        "wool":0,
        "ore":0,
        "grain":0,
        "lumber":0
    }

    # Game Initialization
    def __init__(self, num_of_players, gamemode):

        # Based on the Number of Players
        for _ in list(range(num_of_players)):

            # Add a player to the player list
            self.players.append(Player())

        # Game was initialized in beginner mode
        if (gamemode == "Beginner"):
            #------- beginner board --------
            # Create 70 Edges
            edge_list = []

        for player in self.players:
            player.roads -= 2
            player.settlements -= 2

    def end():
        for player in self.players:
            if (player.points == 10):
                print(player.colour + " wins!")
                return True

    def turn(player):

