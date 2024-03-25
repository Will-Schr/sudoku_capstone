# pylint: disable=wrong-import-position, no-member, unexpected-keyword-arg
# I have no clue why pylint is throwing the second error
#TODO: find more elegant fix to the sys path append bs
"""
Tests accuracy of basic scan functions of the board class
"""
import unittest
import sys
sys.path.append(".")

from sudoku_package.Board import board
from sudoku_package.Square import square


class Test_hor_comp(unittest.TestCase):
    """Tests horizontal comparison function"""
    def test_hor_comp_1(self):
        """Test 1 of horizontal scan"""
        test_row = board(([[square(9), square(pos_in=[1,2,3,4,5,6,7,8,9])]]))
        test_row.hor_comp()
        solution_row = board(([[square(9), square(pos_in=[1,2,3,4,5,6,7,8])]]))
        self.assertEqual(test_row.test_out_table(),solution_row.test_out_table())
        print(test_row.test_out_table())
        print(solution_row.test_out_table())

class Test_vert_comp(unittest.TestCase):
    """Tests vertical comparison function"""
    def test_vert_comp_1(self):
        """
        Basic test to ensure that vertical comparison can solve based on existing values
        """
        test_board = board(([square(1),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(2),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(3),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(4),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(5),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(6),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(7),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(8),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()]))
        solution_board = board(([square(1),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(2),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(3),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(4),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(5),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(6),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(7),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(8),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(9),square(),square(),square(),square(),square(),square(),square(),square()]))
        test_board.vert_comp()
        self.assertEqual(test_board.test_out_table(),solution_board.test_out_table())
    

if __name__== '__main__':
    unittest.main()
