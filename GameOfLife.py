def conways_game_of_life(initial_state, num_generations):
    """
    Program for Conway's Game of Life for a given initial state and number of generations.

    Parameters:
    initial_state (list): List of coordinate pairs representing the initial live cells.
    num_generations (int): Number of generations to simulate.

    Returns: None
    """

    def count_live_neighbors(board, i, j):
        """
        Counts the number of live neighbors for a cell at position (i, j) in the board.

        Parameters:
        board (list): 2D list representing the game board.
        i (int): Row index of the cell.
        j (int): Column index of the cell.

        Returns:
        int: Number of live neighbors.
        """
        live_count = 0
        for x in range(max(0, i-1), min(len(board), i+2)):
            for y in range(max(0, j-1), min(len(board[0]), j+2)):
                live_count += board[x][y] if (x, y) != (i, j) else 0
        return live_count

    def apply_rules(board):
        """
        Applies the rules of Conway's Game of Life to the current board and generates a new board.

        Parameters:
        board (list): 2D list representing the game board.

        Returns:
        list: 2D list representing the new game board after applying the rules.
        """
        new_board = [[0] * len(board[0]) for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                live_neighbors = count_live_neighbors(board, i, j)
                if board[i][j] == 1:  # Cell is currently alive
                    if live_neighbors < 2 or live_neighbors > 3:  # Underpopulation or overpopulation
                        new_board[i][j] = 0  # Cell dies
                    else:
                        new_board[i][j] = 1  # Cell remains alive
                else:  # Cell is currently dead
                    if live_neighbors == 3:  # Reproduction
                        new_board[i][j] = 1  # Cell becomes alive
        return new_board

    board = [[0] * 200 for _ in range(200)]
    for cell in initial_state:
        board[cell[0]][cell[1]] = 1

    for generation in range(num_generations):
        board = apply_rules(board)
        live_cells = [[i, j] for i in range(len(board)) for j in range(len(board[0])) if board[i][j] == 1]
        print(f"{generation + 1}: {live_cells}")

# Scenario 1
# conways_game_of_life([[1, 1]], 100)

# Scenario 2
# conways_game_of_life([[5, 5], [6, 5], [7, 5], [5, 6], [6, 6], [7, 6]], 100)
