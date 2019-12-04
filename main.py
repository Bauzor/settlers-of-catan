from board import Board

if __name__ == "__main__":
    game = Board("Beginner")
    for i in list(range(3)):
        for j in list(range(6)):
            print(f"hex {i} vertex {j}")
            print(game.board[0][i].vertices[j])
            print(game.board[0][i].vertices[j].adjacent)
            print("")