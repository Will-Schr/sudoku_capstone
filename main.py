"""
A handy sudoku solving tool
Currently a work in progress
"""
from tkinter import Tk
from sudoku_package.Board import board
from sudoku_package.Display import SudokuBoardGUI

test_board = board()
root = Tk()
root.title("Sudoku")
SudokuBoardGUI(root,test_board)
root.mainloop()
