# pylint: disable=wrong-import-position, no-member, unexpected-keyword-arg
# I have no clue why pylint is throwing the second error
"""
Tests accuracy of hidden and naked functions of the board class
"""
import unittest
import sys
sys.path.append(".")

from sudoku_package.Board import board
from sudoku_package.Square import square


class Test_naked_doubles(unittest.TestCase):
    """Tests matches_h finding naked doubles"""
    def test_naked_double_horizontal(self):
        """
        Test 1 of naked double horizontal; tests first row
        """
        test_board = board(([square(pos_in=[1,2]),square(pos_in=[1,2]),square(8),square(pos_in=[2,4]),square(pos_in=[2,3]),square(pos_in=[1,5]),square(9),square(6),square(7)],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()]))
        solution_board = board(([square(pos_in=[1,2]),square(pos_in=[1,2]),square(8),square(4),square(3),square(5),square(9),square(6),square(7)],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()]))
        test_board.naked_pairs_h()
        solution_board.basic_scans()
        self.assertEqual(test_board.test_out_table(),solution_board.test_out_table())

    def test_naked_double_horizontal_2(self):
        """
        Test 2 of naked double horizontal scan; tests last row
        """
        test_board = board(([square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(pos_in=[1,2]),square(pos_in=[1,2]),square(8),square(pos_in=[2,4]),square(pos_in=[2,3]),square(pos_in=[1,5]),square(9),square(6),square(7)]))
        solution_board = board(([square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(pos_in=[1,2]),square(pos_in=[1,2]),square(8),square(4),square(3),square(5),square(9),square(6),square(7)]))
        test_board.naked_pairs_h()
        solution_board.basic_scans()
        self.assertEqual(test_board.test_out_table(),solution_board.test_out_table())

    def test_naked_double_horizontal_3(self):
        """
        Test 3 of naked double horizontal scan; tests to ensure only doubles are found
        """
        test_board = board(([square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(pos_in=[1,2,3]),square(pos_in=[1,2,3]),square(pos_in=[8,9]),square(pos_in=[2,4]),square(pos_in=[2,3]),square(pos_in=[1,5]),square(pos_in=[8,9]),square(pos_in=[6,8,9]),square(7)]))
        solution_board = board(([square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(pos_in=[1,2,3]),square(pos_in=[1,2,3]),square(pos_in=[8,9]),square(pos_in=[2,4]),square(pos_in=[2,3]),square(pos_in=[1,5]),square(pos_in=[8,9]),square(6),square(7)]))
        test_board.naked_pairs_h()
        solution_board.basic_scans()
        self.assertEqual(test_board.test_out_table(),solution_board.test_out_table())

    def test_naked_double_vertical(self):
        """
        Test 1 of naked double vertical scan; tests first column
        """
        test_board = board(([square(pos_in=[1,2]),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(pos_in=[1,2]),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(8),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(pos_in=[2,4]),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(pos_in=[2,3]),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(pos_in=[1,5]),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(9),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(6),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(7),square(),square(),square(),square(),square(),square(),square(),square()]))
        solution_board = board(([square(pos_in=[1,2]),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(pos_in=[1,2]),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(8),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(4),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(3),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(5),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(9),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(6),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(7),square(),square(),square(),square(),square(),square(),square(),square()]))
        test_board.naked_pairs_v()
        solution_board.basic_scans()
        self.assertEqual(test_board.test_out_table(),solution_board.test_out_table())

    def test_naked_double_vertical_2(self):
        """
        Test 2 of naked double vertical scan; tests last column
        """
        test_board = board(([square(),square(),square(),square(),square(),square(),square(),square(),square(pos_in=[1,2])],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square(pos_in=[1,2])],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square(8)],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square(pos_in=[2,4])],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square(pos_in=[2,3])],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square(pos_in=[1,5])],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square(9)],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square(6)],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square(7)]))
        solution_board = board(([square(),square(),square(),square(),square(),square(),square(),square(),square(pos_in=[1,2])],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square(pos_in=[1,2])],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square(8)],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square(4)],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square(3)],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square(5)],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square(9)],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square(6)],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square(7)]))
        test_board.naked_pairs_v()
        solution_board.basic_scans()
        self.assertEqual(test_board.test_out_table(),solution_board.test_out_table())

    def test_naked_double_vertical_3(self):
        """
        Test 3 of naked double vertical scan; tests to ensure only doubles are found
        """
        test_board = board(([square(pos_in=[1,2,3]),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(pos_in=[1,2,3]),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(pos_in=[8,9]),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(pos_in=[2,4]),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(pos_in=[2,3]),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(pos_in=[1,5]),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(pos_in=[8,9]),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(pos_in=[6,8,9]),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(7),square(),square(),square(),square(),square(),square(),square(),square()]))
        solution_board = board(([square(pos_in=[1,2,3]),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(pos_in=[1,2,3]),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(pos_in=[8,9]),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(pos_in=[2,4]),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(pos_in=[2,3]),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(pos_in=[1,5]),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(pos_in=[8,9]),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(6),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(7),square(),square(),square(),square(),square(),square(),square(),square()]))
        test_board.naked_pairs_v()
        solution_board.basic_scans()
        self.assertEqual(test_board.test_out_table(),solution_board.test_out_table())

    def test_naked_double_square(self):
        """
        Test 1 of naked double vertical scan; tests first square
        """
        test_board = board(([square(pos_in=[1,2,3]),square(pos_in=[1,2,3]),square(pos_in=[8,9]),square(),square(),square(),square(),square(),square()],
                [square(pos_in=[2,4]),square(pos_in=[2,3]),square(pos_in=[1,5]),square(),square(),square(),square(),square(),square()],
                [square(pos_in=[8,9]),square(pos_in=[6,8,9]),square(7),square(),square(),square(),square(),square(),square()],
                [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                [square(),square(),square(),square(),square(),square(),square(),square(),square()]))
        solution_board = board(([square(pos_in=[1,2,3]),square(pos_in=[1,2,3]),square(pos_in=[8,9]),square(),square(),square(),square(),square(),square()],
                [square(pos_in=[2,4]),square(pos_in=[2,3]),square(pos_in=[1,5]),square(),square(),square(),square(),square(),square()],
                [square(pos_in=[8,9]),square(6),square(7),square(),square(),square(),square(),square(),square()],
                [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                [square(),square(),square(),square(),square(),square(),square(),square(),square()]))
        test_board.naked_pairs_s()
        solution_board.basic_scans()
        self.assertEqual(test_board.test_out_table(),solution_board.test_out_table())

    def test_naked_double_square_2(self):
        """
        Test 2 of naked double square scan; tests last square
        """
        test_board = board(([square(),square(),square(),square(),square(),square(),square(),square(),square()],
                [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                [square(),square(),square(),square(),square(),square(),square(pos_in=[1,2,3]),square(pos_in=[1,2,3]),square(pos_in=[8,9])],
                [square(),square(),square(),square(),square(),square(),square(pos_in=[2,4]),square(pos_in=[2,3]),square(pos_in=[1,5])],
                [square(),square(),square(),square(),square(),square(),square(pos_in=[8,9]),square(pos_in=[6,8,9]),square(7)]))
        solution_board = board(([square(),square(),square(),square(),square(),square(),square(),square(),square()],
                [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                [square(),square(),square(),square(),square(),square(),square(pos_in=[1,2,3]),square(pos_in=[1,2,3]),square(pos_in=[8,9])],
                [square(),square(),square(),square(),square(),square(),square(pos_in=[2,4]),square(pos_in=[2,3]),square(pos_in=[1,5])],
                [square(),square(),square(),square(),square(),square(),square(pos_in=[8,9]),square(6),square(7)]))
        test_board.naked_pairs_s()
        solution_board.basic_scans()
        self.assertEqual(test_board.test_out_table(),solution_board.test_out_table())

    def test_naked_double_square_3(self):
        """
        Test 3 of naked double square scan; tests to ensure only doubles are found
        """
        test_board = board(([square(pos_in=[1,2,3]),square(pos_in=[1,2,3]),square(pos_in=[8,9]),square(),square(),square(),square(),square(),square()],
                   [square(pos_in=[2,4]),square(pos_in=[2,3]),square(pos_in=[1,5]),square(),square(),square(),square(),square(),square()],
                   [square(pos_in=[8,9]),square(pos_in=[6,8,9]),square(7),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()]))
        solution_board = board(([square(pos_in=[1,2,3]),square(pos_in=[1,2,3]),square(pos_in=[8,9]),square(),square(),square(),square(),square(),square()],
                   [square(pos_in=[2,4]),square(pos_in=[2,3]),square(pos_in=[1,5]),square(),square(),square(),square(),square(),square()],
                   [square(pos_in=[8,9]),square(6),square(7),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()]))
        test_board.naked_pairs_s()
        solution_board.basic_scans()
        self.assertEqual(test_board.test_out_table(),solution_board.test_out_table())

class Test_hidden_doubles(unittest.TestCase):
    """Tests matches_h finding hidden doubles"""
    def test_hidden_double_1(self):
        """Test 1 of hidden double"""
        test_row = board([[square(pos_in=[1,2,3]), square(pos_in=[1,2,3]), square(pos_in=[3,4]), square(pos_in=[3,5])]])
        solution_row = board([[square(pos_in=[1,2]), square(pos_in=[1,2]), square(pos_in=[3,4]), square(pos_in=[3,5])]])
        test_row.hidden_pairs_h()
        self.assertEqual(test_row.test_out_table(),solution_row.test_out_table())

    def test_hidden_double_2(self):
        """Test 2 of hidden double"""
        test_row = board([[square(pos_in=[1,3,5]), square(pos_in=[5,6,7]), square(pos_in=[1,3,7]), square(pos_in=[8,9])]])
        solution_row = board([[square(pos_in=[1,3]), square(pos_in=[5,6,7]), square(pos_in=[1,3]), square(pos_in=[8,9])]])
        test_row.hidden_pairs_h()
        self.assertEqual(test_row.test_out_table(),solution_row.test_out_table())

# class Test_naked_triples(unittest.TestCase):
#     """Tests matches_h finding naked triples"""
#     def test_naked_triple_1(self):
#         """Test 1 of naked triple"""
#         test_row = board([square(pos_in=[1,2,3]), square(pos_in=[1,2,3]), square(pos_in=[3,4]), square(pos_in=[3,5])])
#         solution_row = board([square(pos_in=[1,2,3]), square(pos_in=[1,2,3]), square(pos_in=[4]), square(pos_in=[5])])
#         self.assertEqual(test_row.test_out_row(),solution_row.test_out_row())

if __name__== '__main__':
    unittest.main()
