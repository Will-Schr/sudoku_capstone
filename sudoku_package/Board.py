# pylint: disable=no-member
"""
Module that contains the board class
"""
from sudoku_package.Square import square

class board:
    """Class that holds and modifies sudoku table"""
    def __init__(self, table_in = None):
        if table_in is None:
            self.table = [[],[],[],[],[],[],[],[],[]]
        else:
            self.table = table_in
        self.solved = False

    def test_out_row(self):
        """
        Outputs single row as a list for testing purposes
        """
        row_out = []
        for i in self.table:
            row_out.append(i.pos)
        return row_out
    
    def test_out_table(self):
        """
        Outputs table as a list of lists for testing purposes
        """
        row_out = []
        for i in self.table:
            if type(i) == list:
                row_append = []
                for j in i:
                    row_append.append([j.pos,j.value])
                row_out.append(row_append)
            else:
                row_out.append([i.pos,i.value])
        return row_out


    def test_unsolved(self):
        """
        Displays number of unsolved cells
        """
        unsolved = 0
        for i in range(9):
            for j in range(9):
                if not self.table[i][j].value:
                    unsolved += 1
        return unsolved


    # User input/output functions
    def manual_fill_table(self):    # Allows user to fill out table manually
        """
        Fills table through the terminal
        (Currently not used; primarily used for early stages of testing)
        """
        print ("Fill the table by row moving from left to right; use zero for squares which are not filled in.")
        for x in range(9):
            correct = input_valid = False
            while not correct:
                print ("Filling row", x + 1)
                for _ in range(9):
                    usr_val_in = input("Input number: ")
                    self.table[x].append(square(usr_val_in))
                while not input_valid:
                    print ("Is", self.table[x], "correct? (y/n)")
                    usr_in = input()
                    if usr_in.upper() == "Y" or usr_in.upper() == "N":
                        input_valid = True
                    else:
                        print ("Invalid Input, Try Again.")
                if usr_in.upper() == "N":
                    self.table[x].clear()
                    print ("Fill Row Again.")
                    input_valid = False
                else:
                    correct = True

    def print_table(self):  # Could remove ? cases with use of get value function in square class
        """
        Prints table to terminal
        (Currently not used; primarily used for early stages of testing)
        """
        horiz = 0
        for i in self.table:
            vert = 0
            for j in i:
                vert += 1
                if (vert % 3 == 0 and vert < 9):
                    if j.value is False:
                        print ("?","", end="")
                    else:
                        print (j.value,"", end="")
                    print ("|",end=" ")
                else:
                    if j.value is False:    # If value is 0 (unknown) then display as "?"
                        print ("?","  ", end="")
                    else:
                        print (j.value,"  ", end="")
            horiz += 1
            if (horiz % 3 == 0 and horiz < 9):
                print ("\n")
                for _ in range(33):
                    print ("-",end="")
            print("\n")
        print ("\n")

    # Sudoku solving functions (return true/false if they make change)
    def fill_squares(self):
        """
        Fills squares in board that only have one possibile answer
        """
        change = False
        for i in self.table:
            for j in i:
                if len(j.pos) == 1: #if there is only one item in list
                    j.set_val(j.pos[0])
                    change = True
        return change

    def hor_comp(self):
        """
        Adjusts possible values in each square; scanning by row
        """
        for i in self.table:
            temp_table = []
            for j in i:
                if len(j.pos) == 0:
                    temp_table.append(j.value)
            for k in i:
                k.pos = [x for x in k.pos if x not in temp_table]   # TODO: test check else if continue makes faster
        return self.fill_squares()

    def vert_comp(self):    # Is there a cleaner way?
        """
        Adjusts possible values in each square; scanning by column
        """
        for x in range(9):
            temp_table = []
            for i in self.table:
                if len(i[x].pos) == 0:
                    temp_table.append(i[x].value)
            for i in self.table:
                if len(i[x].pos) > 1:
                    i[x].pos = [x for x in i[x].pos if x not in temp_table]
        return self.fill_squares()

    def square_check(self):
        """
        Adjusts possible values in each square; scanning by 3x3 square
        """
        hor_index = vert_index = [0,3,6]
        for h_start in hor_index:
            for v_start in vert_index:
                square_lst = []
                for x in range(3):
                    for y in range (3):
                        if self.table[h_start + x][v_start + y].value != 0:
                            square_lst.append(self.table[h_start + x][v_start + y].value)
                for x in range(3):
                    for y in range (3):
                        self.table[h_start + x][v_start + y].pos = [x for x in self.table[h_start + x][v_start + y].pos if x not in square_lst]
        return  self.fill_squares()

    def num_inst_chk(self): # Checks by number (in progress)
        """
        Checks if there is a square that contains the only instance of a number
        Scans horizontally, vertically, and by square
        """
        for num_check in range(1,10):   #TODO: replace x and y values
            for i in self.table: # Horizontal check
                num_of_instance = 0 # Maybe replace with bool
                index = -1
                input_index = None # Index of value to input
                for j in i:
                    index += 1
                    if j.value == num_check:
                        num_of_instance = 2
                        break
                    elif num_check in j.pos:
                        num_of_instance += 1
                        input_index = index
                        if num_of_instance > 1:
                            break
                if num_of_instance == 1:
                    i[input_index].set_val(num_check)

            for y in range(9): # Vertical check
                num_of_instance = 0
                index = -1
                input_index = None
                for i in self.table:
                    index += 1
                    if i[y].value == num_check:
                        num_of_instance = 2
                        break
                    if num_check in i[y].pos:
                        num_of_instance += 1
                        input_index = index
                        if num_of_instance > 1:
                            break
                if num_of_instance == 1:
                    self.table[input_index][y].set_val(num_check)

            hor_index = vert_index = [0,3,6] #Box Check
            for h_start in hor_index:
                for v_start in vert_index:
                    num_of_instance = 0
                    input_h = -1
                    input_v = -1
                    for x in range(3):
                        for y in range (3):
                            if self.table[h_start + x][v_start + y].value == num_check:
                                num_of_instance = 2
                            if num_check in self.table[h_start + x][v_start + y].pos:
                                num_of_instance += 1
                                if num_of_instance > 1:
                                    break
                                input_h = h_start + x
                                input_v = v_start + y
                    if num_of_instance == 1:
                        self.table[input_h][input_v].set_val(num_check)
        return self.fill_squares()

    #TODO: add function for checking that all squares are correct

    def matches_h(self): # In progress https://www.thonky.com/sudoku/naked-pairs-triples-quads
        """
        Horizontally searches for pairs/triples
        """
        #TODO: Find issue
        # Not overwriting cells
        for row in self.table: # Horizontal Scan
            pos_lst = []
            for box in row:
                for comp_box in pos_lst:
                    if box.pos == comp_box:
                        print("placeholder")
                pos_lst.append(box.pos)
        return self.fill_squares()

    def naked_pairs_h(self):
        """
        Searches for naked pairs horizontally
        """
        nav_lst = list(range(9))
        for row in self.table:
            if not nav_lst:
                break
            first_lst = row[nav_lst[0]].pos
            nav_lst.pop(0)
            if (nav_lst == False):
                continue
            for x in nav_lst:
                if (row[x].pos == first_lst):
                    for j in range(9):
                        if row[j].pos != first_lst:
                            row[j].pos = [g for g in row[j].pos if g not in first_lst]
                nav_lst.remove(x)
        return self.fill_squares()

    def solve(self):
        """
        Solves board using combination of functions
        """
        #TODO: Implement scan funtions into one solve function
        for _ in range(100):
            self.hor_comp()
            self.vert_comp()
            self.square_check()
            self.num_inst_chk()

#TODO: add hidden matches function https://www.thonky.com/sudoku/hidden-pairs-triples-quads