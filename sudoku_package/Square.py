"""
Contains square class
"""
class square:
    """
    Individual sudoku square
    Holds the value of the square and a list of possible values for unsolved squares
    """
    def __init__(self, val_in = False, pos_in = False):
        if pos_in:
            self.pos = pos_in
            self.value = False  
            return
        if val_in is False:
            self.pos = list(range(1,10))
        else:
            self.pos = []   # Using empty adds another easy way to detect finished squares
        self.value = val_in

    def __repr__(self): #Used so manual fill can easily display rows
        if self.value == 0:
            return "?"
        return str(self.value)

    def set_val (self, val_in):
        """Sets value of square"""
        self.pos = []
        self.value = val_in
