from game import Game

# All this file should do is handle basic input and output and call functions from the game

def main():
    command = ""
    # Command interpretter loop
    while (command != "Quit"):
        print("Welcome to Settler of Catan!")
        print("Please choose one of the following options")
        print(" - Instructions")
        print(" - Beginner [number of players 4]")
        print(" - Advanced [number of players (2-4)]")
        print(" - Expansion [number of players (2-4)]")
        print(" - Quit")
        command = input()

        if ( command == "Instructions" ):
            print("Instructions")

        elif ( command.split()[0] == "Beginner" ):
            # Number of players
            num_of_players = command.split()[1]
            
            # Used to keep track of which player's turn it is
            turn_order = game.players
            turn_order = random.shuffle(turn_order)
            turn_increment = 0

            # Creates an instance of a game and passes it the number of players.
            game = Game(num_of_players, "Beginner")
            
            while (game.end() == False):
                cur_player = turn_order[turn_increment]

                game.turn(cur_player)

                # Dev Card before roll
                if (len(cur_player.dev_cards) > 0):
                    use_dev_card = input("Would you like to use a development card?")
                    if (use_dev_card == "yes"):
                        print("Please indicate the card you would like to use with the number next to the card")
                        for index, card in enumerate(cur_player.dev_cards, 1):
                            print(index + " " + cur_player.dev_cards.type)
                
                # Updates everyones resources
                game.roll()
                
                #trade
                trade = input("Would you like to trade any resources with any other players?")
                if (trade == "yes"):
                    print("Please propose what resource(s) you are accepting and offering")


                #builds/dev purchase

                turn_increment = (turn_increment + 1) % num_of_players


        elif ( command.split()[0] == "Advanced" ):
            print("Advanced")

        elif ( command.split()[0] == "Expansion" ):
            print("Expansion")

if __name__ == "__main__":
    main()
