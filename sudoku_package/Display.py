# pylint: disable=wrong-import-position, too-many-instance-attributes
"""
Module holding the Sudoku GUI class
"""
import tkinter as tk
import sys
sys.path.append(".")
from sudoku_package.Board import board
from sudoku_package.Square import square

class SudokuBoardGUI:
    """
    This class will serve as the implementation of the board's GUI. The design logic follows this hierarchy:
    1. Initialization method
    2. Board display method
    3. Traversal methods
    4. Input method
    5. Delete method
    6. Highlight cell method
    7. Clear board method
    8. Solve method 
    """
    def __init__(self, master, board_in):
        """The init function initializes the GUI"""
        #First, we want to initialize our board, columns, rows, and canvas.
        self.master = master
        self.current_row, self.current_col = 0, 0

        self.canvas = tk.Canvas(master, width=450, height=450, highlightthickness=0)
        self.canvas.pack()

        #This will call the draw_grid() function.
        self.draw_grid()

        #This contains all of my bindings. This should have arrow key traversal functionality, delete functionality, and input
        #functionality
        master.bind('<Key>', self.input_number)
        master.bind('<BackSpace>', self.delete_number)
        self.canvas.bind('<Button-1>', self.mouse_click)
        master.bind('<Left>', self.move_left)
        master.bind('<Right>', self.move_right)
        master.bind('<Up>', self.move_up)
        master.bind('<Down>', self.move_down)

        #This creates the puzzle/board.
        self.sudBoard = board_in

        #This is for the highlighted cell
        self.highlight_cell = None

        #These set up the buttons that will be displayed on the board.
        self.clear_button = tk.Button(master, text="Clear Board", command=self.clear_board)
        self.clear_button.pack()
        self.solve_button = tk.Button(master, text="Solve", command=self.solve_sudoku)
        self.solve_button.pack()

    def draw_grid(self):
        """
        Function that draws a grid on the canvas
        """
        for i in range(10):
            width = 2 if i % 3 == 0 else 1
            self.canvas.create_line(i * 50, 0, i * 50, 450, width=width)
            self.canvas.create_line(0, i * 50, 450, i * 50, width=width)

    def draw_numbers(self):
        """
        Function that draws the numbers in the cell
        """
        self.canvas.delete('numbers')
        for i in range(9):
            for j in range(9):
                num = self.sudBoard.table[i][j].value
                if num != 0:
                    self.canvas.create_text(j * 50 + 25, i * 50 + 25, text=num, tags='numbers')

    def mouse_click(self, event):
        """
        Functionality for mouse click
        """
        col = event.x // 50
        row = event.y // 50
        if 0 <= row < 9 and 0 <= col < 9:
            self.current_row = row
            self.current_col = col
            self.draw_highlight()

    def move_left(self, event):
        """
        Functionality for selecting and highlighting square to the left
        Going all the way to the left takes you to the previous row
        Going all the way to the start takes you to the end of the board
        """
        if self.current_col == 0:
            if self.current_row == 0:
                self.current_row,self.current_col = 8,8
            else:
                self.current_col = 8
                self.current_row -= 1
        else:
            self.current_col -= 1
        self.draw_highlight()
        self.canvas.focus_set()

    def move_right(self, event):
        """
        Functionality for selecting and highlighting square to the right
        Going all the way to the right takes you to the next row
        Going all the way to the end takes you to the start of the board
        """
        if self.current_col == 8:
            if self.current_row == 8:
                self.current_row, self.current_col = 0,0
            else:
                self.current_col = 0
                self.current_row += 1
        else:
            self.current_col += 1
        self.draw_highlight()
        self.canvas.focus_set()

    def move_up(self, event):
        """
        Functionality for selecting and highlighting square upwards
        Going up all the way up takes you to the previous column
        Going all the way to the start takes you to the end of the board
        """
        if self.current_row == 0:
            if self.current_col == 0:
                self.current_row, self.current_col = 8,8
            else:
                self.current_row = 8
                self.current_col -= 1
        else:
            self.current_row -= 1
        self.draw_highlight()
        self.canvas.focus_set()

    def move_down(self, event):
        """
        Functionality for selecting and highlighting square downwards
        Going down all the way takes you to the next column
        Going all the way to the end takes you to the start of the board
        """
        if self.current_row == 8:
            if self.current_col == 8:
                self.current_row, self.current_col = 0,0
            else:
                self.current_row = 0
                self.current_col += 1
        else:
            self.current_row += 1
        self.draw_highlight()
        self.canvas.focus_set()

    def input_number(self, event):
        """
        Functionality for inputting a number and ONLY a number
        """
        if '1' <= event.char <= '9':
            number = int(event.char)
            self.sudBoard.table[self.current_row][self.current_col].set_val(number)
            self.draw_numbers()

    def delete_number(self,event):
        """
        Functionality for deleting a number
        """
        if self.sudBoard.table[self.current_row][self.current_col].value:
            self.sudBoard.table[self.current_row][self.current_col] = square()
            self.draw_numbers()
            self.canvas.focus_set()

    def draw_highlight(self):
        """
        Functionality for creating the highlight border
        """
        if self.highlight_cell:
            self.canvas.delete(self.highlight_cell)
        x0, y0 = self.current_col * 50, self.current_row * 50
        x1, y1 = x0 + 50, y0 + 50
        self.highlight_cell = self.canvas.create_rectangle(x0, y0, x1, y1, outline="blue", width=2)

    def clear_board(self):
        """
        Function to clear the board
        """
        self.sudBoard = board(([square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()]))
        self.draw_numbers()

    def solve_sudoku(self):
        """
        Function to call the solve function within board class for the board
        """
        self.sudBoard.solve()
        self.sudBoard.print_table()
        self.draw_numbers()

def main():
    """
    main for testing purposes
    """
    root = tk.Tk()
    root.title("Sudoku")
    test_board = board()
    SudokuBoardGUI(root,test_board)
    root.mainloop()

if __name__ == "__main__":
    main()
