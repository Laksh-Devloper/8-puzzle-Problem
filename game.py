def puzzle_game():
    import random

    blocks = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    shuffle = random.sample(blocks, len(blocks))
    puzzle = [[shuffle[i + j] for i in range(0, len(shuffle), 3)] for j in range(3)]

    def print_puzzle():
        for i in puzzle:
            print(*i)
        print("\n")

    print_puzzle()

    while True:
        move = input("Enter the number you want to move (or q to quit): ")
        if move == "q":
            break

        move = int(move)
        for i in range(3):
            for j in range(3):
                if puzzle[i][j] == move:
                    x, y = i, j

        if x > 0 and puzzle[x - 1][y] == 0:
            puzzle[x][y], puzzle[x - 1][y] = puzzle[x - 1][y], puzzle[x][y]
        elif x < 2 and puzzle[x + 1][y] == 0:
            puzzle[x][y], puzzle[x + 1][y] = puzzle[x + 1][y], puzzle[x][y]
        elif y > 0 and puzzle[x][y - 1] == 0:
            puzzle[x][y], puzzle[x][y - 1] = puzzle[x][y - 1], puzzle[x][y]
        elif y < 2 and puzzle[x][y + 1] == 0:
            puzzle[x][y], puzzle[x][y + 1] = puzzle[x][y + 1], puzzle[x][y]
        else:
            print("Invalid move\n")
            continue

        print_puzzle()

        if puzzle == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]:
            print("You win!")
            break

if __name__ == "__main__":
    puzzle_game()
