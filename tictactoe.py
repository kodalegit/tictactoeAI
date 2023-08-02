"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None

class InvalidMoveError(Exception):
    pass


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count_x = 0
    count_o = 0
    for rows in board:
        for play in rows:
            if play == X:
                count_x +=1
            elif play == O:
                count_o +=1
    
    if count_x == count_o:
        return X
    elif count_o < count_x:
        return O
    
def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] is EMPTY:
                moves.add((i, j))
    
    return moves
            

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0]][action[1]] is not None:
        raise InvalidMoveError("This is an invalid move")
    else:
        new_board = copy.deepcopy(board)
        move = player(board)
        new_board[action[0]][action[1]] = move

        return new_board    


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        # horizontal check
        if board[i][0] == board [i][1] == board[i][2]:
            return board[i][0]
        # vertical check
        elif board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]
        
    #diagonal check
    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    elif board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]         
    
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    count = 0
    for rows in board:
        for play in rows:
            if play is EMPTY:
                count +=1

    if winner(board) is None and count > 0:
        return False
    elif winner(board) is None and count == 0:
        return True
    else:
        return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """    
    player = winner(board)
    if player == X:
        return 1
    elif player == O:
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        mover = player(board)
        if mover == X:
            _, decision = maximum_val(board)
            
        else:
            _, decision = minimum_val(board)
            
        return decision



def maximum_val(board):
    if terminal(board):
        return utility(board), None
    
    v = -math.inf 
    best_move = None

    moves = actions(board)
    for move in moves:
        new_board = result(board, move)
                   
        min_val, _ = (minimum_val(new_board))

        if min_val > v:
            v = min_val
            best_move = move

    return v, best_move

def minimum_val(board):
    if terminal(board):
        return utility(board), None
    
    v = math.inf
    best_move = None

    moves = actions(board)
    for move in moves:
        new_board = result(board, move)
       
        max_val, _ = (maximum_val(new_board))

        if max_val < v:
            v = max_val
            best_move = move


    return v, best_move


