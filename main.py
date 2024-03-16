"""
A handy sudoku solving tool
Currently a work in progress
"""
from tkinter import Tk
from sudoku_package.Board import board
from sudoku_package.Square import square
from sudoku_package.Display import board_UI


test_board = ([square(),square(),square(5),square(),square(7),square(8),square(),square(),square()],
                   [square(),square(7),square(),square(4),square(),square(),square(),square(),square()],
                   [square(2),square(),square(),square(5),square(6),square(1),square(3),square(7),square(4)],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(4),square(5),square(2),square(1),square(8)],
                   [square(),square(),square(),square(),square(3),square(2),square(4),square(9),square()],
                   [square(),square(),square(),square(9),square(),square(),square(),square(),square(1)],
                   [square(3),square(),square(1),square(),square(),square(7),square(6),square(),square()],
                   [square(4),square(),square(9),square(),square(),square(),square(8),square(),square()])

Board_in = board(test_board)
root = Tk()
board_UI(root,Board_in)
print("WINDOW CLOSED")