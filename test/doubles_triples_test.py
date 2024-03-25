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


class Test_naked_doubles(unittest.TestCase):
    """Tests matches_h finding naked doubles"""
    def test_naked_double_1(self):
        """Test 1 of naked double"""
        test_row = board([square(pos_in=[1,2]), square(pos_in=[1,2]), square(pos_in=[1,3]), square(pos_in=[2,5])])
        solution_row = board([square(pos_in=[1,2]), square(pos_in=[1,2]), square(pos_in=[1]), square(pos_in=[5])])
        self.assertEqual(test_row.test_out_row(),solution_row.test_out_row())

    def test_naked_double_2(self):
        """Test 2 of naked double"""
        test_row = board([square(pos_in=[1,5]), square(pos_in=[1,2]), square(pos_in=[2,3]), square(pos_in=[1,2])])
        solution_row = board([square(pos_in=[5]), square(pos_in=[1,2]), square(pos_in=[3]), square(pos_in=[1,2])])
        self.assertEqual(test_row.test_out_row(),solution_row.test_out_row())

    def test_naked_double_3(self):
        """Test 3 of naked double"""
        test_row = board([square(pos_in=[1,2]), square(pos_in=[7,8]), square(pos_in=[1,2]), square(pos_in=[7,9]), square(pos_in=[1,3]), square(pos_in=[2,5]), square(pos_in=[7,8])])
        solution_row = board([square(pos_in=[1,2]), square(pos_in=[7,8]), square(pos_in=[1,2]), square(pos_in=[9]), square(pos_in=[1]), square(pos_in=[5]), square(pos_in=[7,8])])
        self.assertEqual(test_row.test_out_row(),solution_row.test_out_row())

class Test_hidden_doubles(unittest.TestCase):
    """Tests matches_h finding hidden doubles"""
    def test_hidden_double_1(self):
        """Test 1 of hidden double"""
        test_row = board([square(pos_in=[1,2,3]), square(pos_in=[1,2,3]), square(pos_in=[3,4]), square(pos_in=[3,5])])
        solution_row = board([square(pos_in=[1,2]), square(pos_in=[1,2]), square(pos_in=[3,4]), square(pos_in=[3,5])])
        self.assertEqual(test_row.test_out_row(),solution_row.test_out_row())

    def test_hidden_double_2(self):
        """Test 2 of hidden double"""
        test_row = board([square(pos_in=[1,3,5]), square(pos_in=[5,6,7]), square(pos_in=[1,3,7]), square(pos_in=[8,9])])
        solution_row = board([square(pos_in=[1,3]), square(pos_in=[5,6,7]), square(pos_in=[1,3]), square(pos_in=[8,9])])
        self.assertEqual(test_row.test_out_row(),solution_row.test_out_row())

class Test_naked_triples(unittest.TestCase):
    """Tests matches_h finding naked triples"""
    def test_naked_triple_1(self):
        """Test 1 of naked triple"""
        test_row = board([square(pos_in=[1,2,3]), square(pos_in=[1,2,3]), square(pos_in=[3,4]), square(pos_in=[3,5])])
        solution_row = board([square(pos_in=[1,2,3]), square(pos_in=[1,2,3]), square(pos_in=[4]), square(pos_in=[5])])
        self.assertEqual(test_row.test_out_row(),solution_row.test_out_row())

if __name__== '__main__':
    unittest.main()