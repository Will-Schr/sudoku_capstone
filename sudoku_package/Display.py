"""
GUI for the sudoku solver
"""
from tkinter import Canvas, Frame, Button, BOTH, TOP, BOTTOM
import math

MARGIN = 20  # Pixels around the board
SIDE = 50  # Width of every board cell.
WIDTH = HEIGHT = MARGIN * 2 + SIDE * 9  # Width and height of the whole board

class board_UI(Frame):
    """
    Holds information/functionality for operating GUI
    """
    def __init__(self, parent, board):
        self.board = board
        Frame.__init__(self, parent)
        self.parent = parent

        self.row, self.col = -1, -1
        self.cell_clicked = [-1, -1] # Used to specify which cell is selected when clicked by the user for adding new numbers; defaults to -1 when no cell is selected
        self.__initUI()

    def __initUI(self):
        self.parent.title("Sudoku")
        self.pack(fill=BOTH, expand=1)
        self.canvas = Canvas(self,
                             width=WIDTH,
                             height=HEIGHT)
        self.canvas.pack(fill=BOTH, side=TOP)
        solve_button = Button(self,
                              text="Solve!",
                              command=self.board.solve) #TODO: Need to add solve command
        solve_button.pack(fill=BOTH, side=BOTTOM)

        self.__draw_grid()
        self.__draw_puzzle()
        self.canvas.bind("<Button-1>", self.__cell_click) #TODO: Find out how this works
        # self.canvas.bind("<Key>", self.__key_pressed)
        self.parent.mainloop()


    def __draw_grid(self):
        """
        Draws grid divided with blue lines into 3x3 squares
        """
        for i in range(10):
            color = "blue" if i % 3 == 0 else "gray"

            x0 = MARGIN + i * SIDE
            y0 = MARGIN
            x1 = MARGIN + i * SIDE
            y1 = HEIGHT - MARGIN
            self.canvas.create_line(x0, y0, x1, y1, fill=color)

            x0 = MARGIN
            y0 = MARGIN + i * SIDE
            x1 = WIDTH - MARGIN
            y1 = MARGIN + i * SIDE
            self.canvas.create_line(x0, y0, x1, y1, fill=color)

    def __draw_puzzle(self):
        self.canvas.delete("numbers")
        for i in range(9):
            for j in range(9):
                answer = self.board.table[i][j].value
                if answer:
                    x = MARGIN + j * SIDE + SIDE / 2
                    y = MARGIN + i * SIDE + SIDE / 2
                    # original = self.game.start_puzzle[i][j]
                    # color = "black" if answer == original else "sea green"
                    color = "black"
                    print(answer,"  x:",x,"y:",y)
                    self.canvas.create_text(
                        x, y, text=answer, tags="numbers", fill=color
                    )

    def __cell_click(self,event):
        print("CLICK RECIEVED") # Debug only
        #TODO: add functionality to select cell based on canvas coordinates
        cursor_x = event.x
        cursor_y = event.y
        if ((cursor_x < MARGIN) or (cursor_x > WIDTH - MARGIN)) or ((cursor_y < MARGIN) or (cursor_y > HEIGHT - MARGIN)):
            self.cell_clicked = [-1,-1]
            return
        column_clicked = math.floor((cursor_x - MARGIN) / 50)
        row_clicked = math.floor((cursor_y - MARGIN) / 50)

        self.cell_clicked = [row_clicked, column_clicked]
        print("Cell location:",self.cell_clicked)
        print("Cell value:",self.board.table[self.cell_clicked[0]][self.cell_clicked[1]].value)