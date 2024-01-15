class SudokuSolver:
    """
    Class to solve a Sudoku board.

    Attributes:
    - board: list of lists
        The Sudoku board represented as a 9x9 grid.
    """

    def __init__(self, board):
        """
        Constructor to instantiate the SudokuSolver class.

        Parameters:
        - board: list of lists
            The initial Sudoku board with empty cells represented as 0.
        """

        self.board = board

    def solve_sudoku(self):
        """
        Solves the Sudoku board using backtracking algorithm.

        Returns:
        - bool:
            True if the Sudoku board is solvable, False otherwise.
        """

        # Find an empty cell on the board
        empty_cell = self.find_empty_cell()

        # If there are no empty cells, the board is solved
        if not empty_cell:
            return True

        # Unpack the row and column of the empty cell
        row, col = empty_cell

        # Try different numbers from 1 to 9
        for num in range(1, 10):
            # Check if the number is valid in the current position
            if self.is_valid(num, row, col):
                # Place the number in the current position
                self.board[row][col] = num

                # Recursively solve the Sudoku board
                if self.solve_sudoku():
                    return True

                # If the current number doesn't lead to a solution, backtrack
                self.board[row][col] = 0

        # If no number can be placed in the current position, the board is unsolvable
        return False

    def find_empty_cell(self):
        """
        Finds an empty cell (cell with value 0) on the Sudoku board.

        Returns:
        - tuple:
            The row and column indices of the empty cell, or None if no empty cell is found.
        """

        for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0:
                    return row, col

        return None

    def is_valid(self, num, row, col):
        """
        Checks if a number is valid in the current position on the Sudoku board.

        Parameters:
        - num: int
            The number to be checked.
        - row: int
            The row index of the current position.
        - col: int
            The column index of the current position.

        Returns:
        - bool:
            True if the number is valid in the current position, False otherwise.
        """

        # Check if the number is already present in the same row
        for i in range(9):
            if self.board[row][i] == num:
                return False

        # Check if the number is already present in the same column
        for i in range(9):
            if self.board[i][col] == num:
                return False

        # Check if the number is already present in the same 3x3 box
        box_row = (row // 3) * 3
        box_col = (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if self.board[box_row + i][box_col + j] == num:
                    return False

        return True


# Example usage of the SudokuSolver class:

# Define the Sudoku board
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Create an instance of SudokuSolver
solver = SudokuSolver(board)

# Solve the Sudoku board
if solver.solve_sudoku():
    # Print the solved board
    for row in solver.board:
        print(row)
else:
    print("No solution exists for the given Sudoku board.")