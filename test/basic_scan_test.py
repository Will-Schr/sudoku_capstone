# pylint: disable=wrong-import-position, no-member, unexpected-keyword-arg
# I have no clue why pylint is throwing the second error
#TODO: find more elegant fix to the sys path append bs
"""
Tests accuracy of matches_h function of the board class
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

if __name__== '__main__':
    unittest.main()
