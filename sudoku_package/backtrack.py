"""
Module that contains the backtracking solve function
"""
import copy
from sudoku_package.Square import square
from sudoku_package.Board import board

def backtrack_solve(board_in:board):
    """
    Recursive function to solve sudoku board using backtracking.
    """
    if board_in.table[0][0] == 5:
        print("ok")
    if board_in.is_solved():
        return board_in
    board_in.basic_scans()
    if board_in.test_unsolved() == 0:
        if board_in.is_solved():
            return board_in
        return
    nxt_loc = board_in.get_next_unsolved()
    if not board_in.table[nxt_loc[0]][nxt_loc[1]].pos:
        return
    for pos_val in board_in.table[nxt_loc[0]][nxt_loc[1]].pos:
        next_board = copy.deepcopy(board_in)
        next_board.table[nxt_loc[0]][nxt_loc[1]].set_val(pos_val)
        check_board = backtrack_solve(next_board)
        if check_board is not None:
            if check_board.is_solved():
                return check_board
    return
