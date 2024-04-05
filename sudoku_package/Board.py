# pylint: disable=no-member,too-many-branches,too-many-nested-blocks
"""
Module that contains the board class

Classes:
    board
"""
from sudoku_package.Square import square

class board:
    """
    Class that holds and modifies sudoku table.

    Attributes:
        table(list): list of lists of square classes to represent sudoku board
        solved (bool): status if board is solved
    """
    def __init__(self, table_in:list = None):
        if table_in is None:
            self.table = [[square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()]]
        else:
            self.table = table_in
        self.solved = False #TODO: needs implmentation


    ##### Board Maintanance functions #####


    def clear_board(self):
        """
        Clears all cells within board
        """
        self.table = [[square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()]]

    def test_out_table(self):
        """
        Outputs table as a list of lists for testing purposes
        """
        row_out = []
        for i in self.table:
            if isinstance(i,list):
                row_append = []
                for j in i:
                    row_append.append([j.pos,j.value])
                row_out.append(row_append)
            else:
                row_out.append([i.pos,i.value])
        return row_out

    def is_valid(self):
        """
        Returns if the board is valid, i.e. doesn't have multiple combinations of a number within it

        Returns:
            (bool): whether board is a valid sudoku board
        """
        # Iterates horizontally
        for row in self.table:
            row_lst = []
            for box in row:
                if box.value == "?":
                    continue
                if box in row_lst:
                    return False
                row_lst.append(box.value)
        # Iterates vertically
        for column_idx in range(9):
            column_lst = []
            for i in self.table:
                if not i[column_idx].value:
                    continue
                if i[column_idx].value in column_lst:
                    return False
                column_lst.append(i[column_idx].value)
        # Iterates in squares
        hor_index = vert_index = [0,3,6]
        for h_start in hor_index:
            for v_start in vert_index:
                square_lst = []
                for x in range(3):
                    for y in range (3):
                        if self.table[h_start + x][v_start + y].value == 0:
                            continue
                        if self.table[h_start + x][v_start + y].value in square_lst:
                            return False
                        square_lst.append(self.table[h_start + x][v_start + y].value)
        return True

    def test_unsolved(self):
        """
        Displays number of unsolved cells

        Returns:
            unsolved(int): number of unsolved squares on the board
        """
        unsolved = 0
        for i in range(9):
            for j in range(9):
                if not self.table[i][j].value:
                    unsolved += 1
        return unsolved


    # User input/output functions
    def manual_fill_table(self):
        """
        Allows the user to fill the table through the terminal
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

    def fill_squares(self):
        """
        Fills squares in board that only have one possible answer

        Returns:
            change(bool): whether the board made was able to fill any squares
        """
        change = False
        for i in self.table:
            for j in i:
                if len(j.pos) == 1: #if there is only one item in list
                    j.set_val(j.pos[0])
                    change = True
        if change:
            self.basic_scans()
        return change


    ##### Basic Sudoku Solving Functions #####


    def hor_comp(self):
        """
        Adjusts possible values in each square; scanning by row

        Returns:
            (bool): result of fill_squares after the scanning completes
        """
        for i in self.table:
            temp_table = []
            for j in i:
                if len(j.pos) == 0:
                    temp_table.append(j.value)
            for k in i:
                k.pos = [x for x in k.pos if x not in temp_table]
        return self.fill_squares()

    def vert_comp(self):
        """
        Adjusts possible values in each square; scanning by column
        
        Returns:
            (bool): result of fill_squares after the scanning completes
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

        Returns:
            (bool): result of fill_squares after the scanning completes
        """
        hor_index = vert_index = [0,3,6] # Indexes used of offsetting for squares
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

    def num_inst_chk(self):
        """
        Checks if there is a square that contains the only instance of a number
        Scans horizontally, vertically, and by square
        
        Returns:
            (bool): result of fill_squares after the scanning completes
        """
        for num_check in range(1,10):
            # Horizontal check
            for i in self.table:
                num_of_instance = 0 # Maybe replace with bool
                index = -1
                input_index = None # Index of value to input
                for j in i:
                    index += 1
                    if j.value == num_check:
                        num_of_instance = 2
                        break
                    if num_check in j.pos:
                        num_of_instance += 1
                        input_index = index
                        if num_of_instance > 1:
                            break
                if num_of_instance == 1:
                    i[input_index].set_val(num_check)

            # Vertical check
            for y in range(9):
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

            #Box Check
            hor_index = vert_index = [0,3,6] # Indexes used of offsetting for squares
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

    def basic_scans(self):
        """
        Function to perform basic sudoku scans
        
        Returns:
            (bool): result of fill_squares after the scanning completes
        """
        return self.hor_comp() or self.vert_comp() or self.num_inst_chk() or self.square_check()


    ##### Naked Set Functions #####


    def naked_sets_h(self):
        """
        Searches for naked sets horizontally
        
        Returns:
            (bool): result of fill_squares after the scanning completes
        """
        for row in self.table:
            nav_lst = list(range(9)) # List of indicies used to iterate
            while nav_lst:
                first_lst = row[nav_lst[0]].pos
                count = 1 # Number of matches
                nav_lst.pop(0)
                if not nav_lst:
                    continue
                indexlst = []
                # Iterates through each unchecked square for matches
                for x in nav_lst:
                    if row[x].pos == first_lst:
                        count += 1
                        indexlst.append(x)
                # If there is matches equal to the length there is a hidden set
                # those values are removed from other squares
                if count == len(first_lst):
                    for j in range(9):
                        if row[j].pos != first_lst:
                            row[j].pos = [g for g in row[j].pos if g not in first_lst]
                # Any matched set squares are removed so they are not checked again
                for index in indexlst:
                    nav_lst.remove(index)
        return self.fill_squares()

    def naked_sets_v(self):
        """
        Searches for naked sets vertically
        
        Returns:
            (bool): result of fill_squares after the scanning completes
        """
        for column in range(9):
            nav_lst = list(range(9)) # List of indicies used to iterate
            while nav_lst:
                first_lst = self.table[nav_lst[0]][column].pos
                count = 1 # Number of matches
                nav_lst.pop(0)
                if not nav_lst:
                    continue
                indexlst = []
                # Iterates through each unchecked square for matches
                for x in nav_lst:
                    if self.table[x][column].pos == first_lst:
                        count += 1
                        indexlst.append(x)
                # If there is matches equal to the length there is a hidden set
                # those values are removed from other squares
                if count == len(first_lst):
                    for j in range(9):
                        if self.table[j][column].pos != first_lst:
                            self.table[j][column].pos = [g for g in self.table[j][column].pos if g not in first_lst]
                # Any matched set squares are removed so they are not checked again
                for index in indexlst:
                    nav_lst.remove(index)
        return self.fill_squares()

    def naked_sets_s(self):
        """
        Searches for naked pairs in square scans

        Returns:
            (bool): result of fill_squares after the scanning completes
        """
        hor_index = vert_index = [0,3,6]
        for h_start in hor_index:
            for v_start in vert_index:
                # Create nav list for scanning in square order
                nav_lst = []
                for x in range(3):
                    for y in range(3):
                        nav_lst.append((h_start + x,v_start + y))
                # Iterates through square pattern to check nav_lst for possible naked pairs
                while nav_lst:
                    first_lst = self.table[nav_lst[0][0]][nav_lst[0][1]].pos
                    count = 1
                    nav_lst.pop(0)
                    if not nav_lst:
                        continue
                    indexlst = []
                    # Checks if possible naked pair exists in subsquare
                    for pair in nav_lst:
                        if self.table[pair[0]][pair[1]].pos == first_lst: # Determines that naked pair exists
                            count += 1
                            indexlst.append(pair)
                    if count == len(first_lst):
                        for x2 in range(3):
                            for y2 in range(3):
                                if self.table[h_start+x2][v_start+y2].pos != first_lst:
                                    self.table[h_start+x2][v_start+y2].pos = [g for g in self.table[h_start+x2][v_start+y2].pos if g not in first_lst]
                    for pair in indexlst:
                        nav_lst.remove(pair)
        return self.fill_squares()

    def naked_set_scan(self):
        """
        Function to perform basic sudoku scans
        
        Returns:
            (bool): result of fill_squares after the scanning completes
        """
        return self.naked_sets_h() or self.naked_sets_v() or self.naked_sets_s()


    ##### Hidden Set Functions #####


    def hidden_pairs_h(self): #TODO: manage seemingly hidden pairs like [3,4,7] and [3,4,7]
        """
        Finds hidden pairs and adjusts pos values accordingly

        Returns:
            (bool): result of fill_squares after the scanning completes
        """
        for row in self.table:
            all_unplaced = []
            unplaced = []
            # Create list of all unplaced values in the row
            for box in row:
                for val in box.pos:
                    all_unplaced.append(val)
            # Create list of all unplaced values that only occur twice
            for u_val in all_unplaced:
                if u_val not in unplaced and all_unplaced.count(u_val) == 2:
                    unplaced.append(u_val)
            for box in row:
                # These nested for loops generate every possible pair from the unplaced list
                for first in range(len(unplaced)-1):
                    for second in range(first + 1,len(unplaced)):
                        first_val = unplaced[first]
                        second_val = unplaced[second]
                        count = 0
                        if first_val in box.pos and second_val in box.pos:
                            # This for loop is used to go through every box and check if there is any other boxes with the hidden pair,
                            # as well as ensure that the pair is exclusive
                            for box_chk in row:
                                if first_val in box_chk.pos or second_val in box_chk.pos:
                                    if first_val in box_chk.pos and second_val in box_chk.pos:
                                        count += 1
                                        if count > 2:
                                            count = 0
                                            break
                                    else:
                                        count = 0
                                        break
                            if count == 2:
                                # TODO: Consider replacing with indicies to prevent extra cycles/nested looping
                                for box_rep in row:
                                    if first_val in box_rep.pos and second_val in box_rep.pos:
                                        # Ordering here isn't necessary, but keeps the pos lists much more clean
                                        if first_val < second_val:
                                            box_rep.pos = [first_val,second_val]
                                        else:
                                            box_rep.pos = [second_val,first_val]
        return self.fill_squares()

    def solve(self):
        """
        Solves board using combination of functions
        """
        for _ in range(100):
            self.basic_scans()
            self.naked_set_scan()
            self.hidden_pairs_h()
#TODO: add pointing pairs function
