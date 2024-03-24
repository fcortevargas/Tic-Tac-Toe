def define_players():
    player1, player2 = None, None
    valid_players = ["O", "X"]
    while player1 not in valid_players:
        player1 = input("Player 1, please choose X or O: ")
        player1 = player1.upper()
        if player1 not in valid_players:
            print("Sorry, you have to choose between X or O.")
    valid_players.remove(player1.upper())
    player2 = valid_players[0]
    print(f"\nPlayer 1 will play using {player1}.")
    print(f"Player 2 will play using {player2}.\n")
    return player1, player2


def initialize_valid_moves():
    valid_moves = []
    for i in range(3):
        for j in range(3):
            valid_moves.append((i, j))
    return valid_moves


def initialize_board(valid_moves):
    return {move: " " for move in valid_moves}


def display_board(board):
    print()
    print([board[(0, 0)], board[(0, 1)], board[(0, 2)]])
    print([board[(1, 0)], board[(1, 1)], board[(1, 2)]])
    print([board[(2, 0)], board[(2, 1)], board[(2, 2)]])
    print()


def is_board_full(board):
    return " " not in board.values()


def is_vertical_win(board):
    vertical_win = False
    j = 0
    while not vertical_win and j < 3:
        equal_entries = board[(0, j)] == board[(1, j)] == board[(2, j)]
        valid_entries = board[(0, j)] != " " and board[(1, j)] != " " and board[(2, j)] != " "
        vertical_win = valid_entries and equal_entries
        j += 1
    return vertical_win


def is_horizontal_win(board):
    horizontal_win = False
    i = 0
    while not horizontal_win and i < 3:
        equal_entries = board[(i, 0)] == board[(i, 1)] == board[(i, 2)]
        valid_entries = board[(i, 0)] != " " and board[(i, 1)] != " " and board[(i, 2)] != " "
        horizontal_win = valid_entries and equal_entries
        i += 1
    return horizontal_win


def is_diagonal_win(board):
    equal_entries = board[(0, 0)] == board[(1, 1)] == board[(2, 2)] or board[(0, 2)] == board[(1, 1)] == board[(2, 0)]
    valid_entries = (board[(0, 0)] != " " and board[(1, 1)] != " " and board[(2, 2)] != " ") or \
                    (board[(0, 2)] != " " and board[(1, 1)] != " " and board[(2, 0)] != " ")
    return equal_entries and valid_entries


def is_game_over(board):
    return is_vertical_win(board) or is_horizontal_win(board) or is_diagonal_win(board) or is_board_full(board)


def process_input_move(move):
    processed = list(filter(lambda x: x.isdigit(), move))
    if len(processed) != 2:
        return None
    return int(processed[0]), int(processed[1])


def next_move(board, player_number, players, valid_moves):
    move = None
    while move not in valid_moves:
        move = input(f"Player {player_number}, please enter your next move (e.g., (1,0)): ")
        move = process_input_move(move)
        if move not in valid_moves:
            print("Sorry, that move is not valid.")
        else:
            board[move] = players[player_number]
    valid_moves.remove(move)
    player_number = 1 if player_number == 2 else 2
    return board, player_number, valid_moves


def main():
    print("Welcome to Tic-Tac-Toe!\n")

    p1, p2 = define_players()
    players = {1: p1, 2: p2}

    valid_moves = initialize_valid_moves()
    board = initialize_board(valid_moves)

    print("Let's start playing!")

    display_board(board)

    current_player_number = 1

    while not is_game_over(board):
        board, current_player_number, valid_moves = next_move(board, current_player_number, players, valid_moves)
        display_board(board)

    if is_diagonal_win(board) or is_horizontal_win(board) or is_vertical_win(board):
        current_player_number = 1 if current_player_number == 2 else 2
        print(f"Player {current_player_number} won the game.")
    else:
        print("No one won the game.")


if __name__ == "__main__":
    main()
