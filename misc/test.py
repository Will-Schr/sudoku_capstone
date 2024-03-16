# pylint: skip-file
import math
MARGIN = 20  # Pixels around the board
SIDE = 50  # Width of every board cell.
WIDTH = HEIGHT = MARGIN * 2 + SIDE * 9  # Width and height of the whole board
cursor_x = 445
cursor_y = 345

if ((cursor_x < MARGIN) or (cursor_x > WIDTH - MARGIN)) or ((cursor_y < MARGIN) or (cursor_y > HEIGHT - MARGIN)):
    cell_clicked = [-1,-1]
column_clicked = math.floor((cursor_x - MARGIN) / 50)
row_clicked = math.floor((cursor_y - MARGIN) / 50)

cell_clicked = [row_clicked, column_clicked]
print (cell_clicked)
