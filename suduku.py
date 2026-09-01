
class Sudoku:
    # Spin up a completely blank 9x9 grid
    def __init__(self):
        self.board = [[0] * 9 for _ in range(9)]

    # Drop a number into a specific square (0-indexed)
    def insert(self, row, col, num):
        if 1 <= num <= 9:
            self.board[row][col] = num
        else:
            print("Hold up! Sudoku only uses numbers 1 through 9.")

    # Print it out so it actually looks like a puzzle
    def display(self):
        print("\n=== SUDOKU BOARD ===")
        for r in range(9):
            # Draw horizontal lines to separate 3x3 blocks
            if r % 3 == 0 and r != 0:
                print("-" * 21)
            
            line = ""
            for c in range(9):
                # Draw vertical lines to separate 3x3 blocks
                if c % 3 == 0 and c != 0:
                    line += "| "
                
                # Show dots for empty spaces to make it readable
                val = self.board[r][c]
                line += str(val) + " " if val != 0 else ". "
            print(line)

# Let's set up a quick game
game = Sudoku()
game.insert(0, 0, 5)
game.insert(0, 1, 3)
game.insert(4, 4, 8)
game.insert(8, 8, 9)

# Show off the board
game.display()
