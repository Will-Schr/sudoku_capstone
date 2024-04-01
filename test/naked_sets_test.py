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


class Test_horizontal_naked_sets(unittest.TestCase):
    """
    Tests horizontal naked sets function
    """
    def test_naked_set_horizontal(self):
        """
        Test 1 of naked set horizontal scan; tests first row
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
        test_board.naked_sets_h()
        solution_board.basic_scans()
        self.assertEqual(test_board.test_out_table(),solution_board.test_out_table())

    def test_naked_set_horizontal_2(self):
        """
        Test 2 of naked set horizontal scan; tests last row
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
        test_board.naked_sets_h()
        solution_board.basic_scans()
        self.assertEqual(test_board.test_out_table(),solution_board.test_out_table())

    def test_naked_set_horizontal_3(self):
        """
        Test 3 of naked set horizontal scan; tests to ensure only doubles are found
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
        test_board.naked_sets_h()
        solution_board.basic_scans()
        self.assertEqual(test_board.test_out_table(),solution_board.test_out_table())

    def test_naked_set_horizontal_4(self):
        """
        Test 4 of naked set horizontal scan; tests for detecting multiple naked pairs
        """
        test_board = board(([square(pos_in=[1,2]),square(pos_in=[1,2]),square(8),square(pos_in=[3,4]),square(pos_in=[3,4]),square(pos_in=[1,4,5]),square(9),square(6),square(7)],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()]))
        solution_board = board(([square(pos_in=[1,2]),square(pos_in=[1,2]),square(8),square(pos_in=[3,4]),square(pos_in=[3,4]),square(5),square(9),square(6),square(7)],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()]))
        test_board.naked_sets_h()
        solution_board.basic_scans()
        self.assertEqual(test_board.test_out_table(),solution_board.test_out_table())

    def test_naked_set_horizontal_5(self):
        """
        Test 5 of naked set horizontal scan; tests for detecting naked triples
        """
        test_board = board(([square(pos_in=[1,2,3]),square(pos_in=[1,2,3]),square(pos_in=[1,2,3]),square(pos_in=[1,5]),square(pos_in=[3,4]),square(pos_in=[2,8]),square(9),square(6),square(7)],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()]))
        solution_board = board(([square(pos_in=[1,2,3]),square(pos_in=[1,2,3]),square(pos_in=[1,2,3]),square(5),square(4),square(8),square(9),square(6),square(7)],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()]))
        test_board.naked_sets_h()
        solution_board.basic_scans()
        self.assertEqual(test_board.test_out_table(),solution_board.test_out_table())

class Test_vertical_naked_sets(unittest.TestCase):
    """
    Tests vertical naked sets function
    """
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

    def test_naked_double_vertical_4(self):
        """
        Test 4 of naked double vertical; tests for detecting multiple naked pairs
        """
        test_board = board(([square(pos_in=[1,2]),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(pos_in=[1,2]),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(8),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(pos_in=[3,4]),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(pos_in=[3,4]),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(pos_in=[1,4,5]),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(9),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(6),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(7),square(),square(),square(),square(),square(),square(),square(),square()]))
        solution_board = board(([square(pos_in=[1,2]),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(pos_in=[1,2]),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(8),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(pos_in=[3,4]),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(pos_in=[3,4]),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(5),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(9),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(6),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(7),square(),square(),square(),square(),square(),square(),square(),square()]))
        test_board.naked_pairs_v()
        solution_board.basic_scans()
        self.assertEqual(test_board.test_out_table(),solution_board.test_out_table())

class Test_square_naked_sets(unittest.TestCase):
    """
    Tests square naked sets function
    """
    def test_naked_double_square(self):
        """
        Test 1 of naked double square scan; tests first square
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

    def test_naked_double_square_4(self):
        """
        Test 4 of naked double square; tests for detecting multiple naked pairs
        """
        test_board = board(([square(pos_in=[1,2]),square(pos_in=[3,4]),square(9),square(),square(),square(),square(),square(),square()],
                   [square(pos_in=[1,2]),square(pos_in=[3,4]),square(6),square(),square(),square(),square(),square(),square()],
                   [square(8),square(pos_in=[1,4,5]),square(7),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()]))
        solution_board = board(([square(pos_in=[1,2]),square(pos_in=[3,4]),square(9),square(),square(),square(),square(),square(),square()],
                   [square(pos_in=[1,2]),square(pos_in=[3,4]),square(6),square(),square(),square(),square(),square(),square()],
                   [square(8),square(5),square(7),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()]))
        test_board.naked_pairs_s()
        solution_board.basic_scans()
        self.assertEqual(test_board.test_out_table(),solution_board.test_out_table())

if __name__== '__main__':
    unittest.main()
