"""
Contains square class
"""
class square:
    """
    Individual sudoku square
    Holds the value of the square and a list of possible values for unsolved squares

    Attributes:
        value(int): value of the sudoku square, set to false when unsolved
        pos(list): list of possible values for square
    
    Methods:
        set_val(): Sets value of square
    """
    def __init__(self, val_in:int = False, pos_in:list = False):
        if pos_in:
            self.pos = pos_in
            self.value = False
            self.solved = False
            return
        if val_in is False:
            self.pos = list(range(1,10))
        else:
            self.pos = []   # Using empty adds another easy way to detect finished squares
        self.value = val_in
        self.solved = False

    def __repr__(self): #Used so manual fill can easily display rows
        if self.value == 0:
            return "?"
        return str(self.value)

    def set_val (self, val_in:int):
        """
        Sets value of square
        """
        self.pos = []
        self.value = val_in
        self.solved = True
