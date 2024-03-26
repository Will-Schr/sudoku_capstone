# pylint: disable=wrong-import-position, no-member
# I have no clue why pylint is throwing no-member error
#TODO: find more elegant fix to the sys path append bs
"""
Tests accuracy of full sudoku solving functionality
"""
import unittest
import sys
sys.path.append(".")

from sudoku_package.Board import board
from sudoku_package.Square import square

class Test_Easy_Sudoku(unittest.TestCase):
    """Tests easy sudoku puzzles"""
    def test_easy_board_1(self):
        """Tests easy sudoku puzzle 1"""
        easy_board = board(([square(),square(1),square(3),square(5),square(),square(),square(4),square(2),square()],
                    [square(),square(8),square(7),square(),square(),square(4),square(),square(),square()],
                    [square(),square(),square(4),square(),square(7),square(9),square(6),square(),square(3)],
                    [square(),square(6),square(2),square(),square(4),square(),square(5),square(),square(8)],
                    [square(),square(),square(),square(),square(5),square(),square(1),square(),square(2)],
                    [square(),square(3),square(8),square(),square(9),square(1),square(),square(),square()],
                    [square(),square(),square(),square(9),square(),square(),square(8),square(),square()],
                    [square(7),square(),square(),square(8),square(1),square(5),square(),square(),square(9)],
                    [square(8),square(9),square(1),square(),square(),square(7),square(2),square(5),square()]))

        solution_board = board(([square(9),square(1),square(3),square(5),square(8),square(6),square(4),square(2),square(7)],
                    [square(6),square(8),square(7),square(3),square(2),square(4),square(9),square(1),square(5)],
                    [square(2),square(5),square(4),square(1),square(7),square(9),square(6),square(8),square(3)],
                    [square(1),square(6),square(2),square(7),square(4),square(3),square(5),square(9),square(8)],
                    [square(4),square(7),square(9),square(6),square(5),square(8),square(1),square(3),square(2)],
                    [square(5),square(3),square(8),square(2),square(9),square(1),square(7),square(6),square(4)],
                    [square(3),square(4),square(5),square(9),square(6),square(2),square(8),square(7),square(1)],
                    [square(7),square(2),square(6),square(8),square(1),square(5),square(3),square(4),square(9)],
                    [square(8),square(9),square(1),square(4),square(3),square(7),square(2),square(5),square(6)]))
        easy_board.solve()
        self.assertEqual(easy_board.test_out_table(), solution_board.test_out_table(), "\n\nUnsolved Squares: " + str(easy_board.test_unsolved()))

    def test_easy_board_2(self):
        """Tests easy sudoku puzzle 2"""
        easy_board = board(([square(),square(),square(),square(),square(6),square(5),square(9),square(2),square(8)],
                   [square(1),square(),square(5),square(),square(2),square(),square(7),square(6),square()],
                   [square(),square(),square(2),square(8),square(),square(),square(),square(),square()],
                   [square(5),square(3),square(),square(4),square(8),square(9),square(),square(),square()],
                   [square(6),square(4),square(),square(7),square(),square(),square(8),square(3),square()],
                   [square(),square(),square(7),square(),square(1),square(),square(),square(4),square(9)],
                   [square(4),square(9),square(),square(),square(),square(8),square(1),square(5),square(7)],
                   [square(),square(1),square(8),square(),square(),square(),square(3),square(),square()],
                   [square(),square(),square(),square(),square(9),square(1),square(2),square(),square()]))

        solution_board = board(([square(3),square(7),square(4),square(1),square(6),square(5),square(9),square(2),square(8)],
                   [square(1),square(8),square(5),square(9),square(2),square(4),square(7),square(6),square(3)],
                   [square(9),square(6),square(2),square(8),square(7),square(3),square(4),square(1),square(5)],
                   [square(5),square(3),square(1),square(4),square(8),square(9),square(6),square(7),square(2)],
                   [square(6),square(4),square(9),square(7),square(5),square(2),square(8),square(3),square(1)],
                   [square(8),square(2),square(7),square(3),square(1),square(6),square(5),square(4),square(9)],
                   [square(4),square(9),square(6),square(2),square(3),square(8),square(1),square(5),square(7)],
                   [square(2),square(1),square(8),square(5),square(4),square(7),square(3),square(9),square(6)],
                   [square(7),square(5),square(3),square(6),square(9),square(1),square(2),square(8),square(4)]))
        easy_board.solve()
        self.assertEqual(easy_board.test_out_table(), solution_board.test_out_table(), "\n\nUnsolved Squares: " + str(easy_board.test_unsolved()))
    
    def test_easy_board_3(self):
        """Tests easy sudoku puzzle 3"""
        easy_board = board(([square(),square(),square(),square(7),square(),square(),square(5),square(),square()],
                   [square(),square(2),square(9),square(),square(3),square(),square(),square(8),square()],
                   [square(7),square(1),square(),square(6),square(8),square(),square(),square(),square()],
                   [square(),square(6),square(7),square(),square(),square(),square(3),square(),square(5)],
                   [square(9),square(),square(),square(),square(2),square(),square(),square(),square()],
                   [square(),square(),square(),square(3),square(),square(),square(),square(7),square(9)],
                   [square(6),square(4),square(2),square(8),square(),square(3),square(),square(1),square(7)],
                   [square(3),square(7),square(),square(4),square(),square(9),square(2),square(5),square(8)],
                   [square(),square(),square(),square(2),square(),square(1),square(6),square(),square()]))

        solution_board = board(([square(4),square(8),square(6),square(7),square(9),square(2),square(5),square(3),square(1)],
                   [square(5),square(2),square(9),square(1),square(3),square(4),square(7),square(8),square(6)],
                   [square(7),square(1),square(3),square(6),square(8),square(5),square(4),square(9),square(2)],
                   [square(1),square(6),square(7),square(9),square(4),square(8),square(3),square(2),square(5)],
                   [square(9),square(3),square(8),square(5),square(2),square(7),square(1),square(6),square(4)],
                   [square(2),square(5),square(4),square(3),square(1),square(6),square(8),square(7),square(9)],
                   [square(6),square(4),square(2),square(8),square(5),square(3),square(9),square(1),square(7)],
                   [square(3),square(7),square(1),square(4),square(6),square(9),square(2),square(5),square(8)],
                   [square(8),square(9),square(5),square(2),square(7),square(1),square(6),square(4),square(3)]))
        easy_board.solve()
        self.assertEqual(easy_board.test_out_table(), solution_board.test_out_table(), "\n\nUnsolved Squares: " + str(easy_board.test_unsolved()))

class Test_Medium_Sudoku(unittest.TestCase):
    """Tests multiple medium sudoku puzzles"""
    def test_medium_board_1(self):
        """Tests medium sudoku puzzle 1"""
        medium_board = board(([square(5),square(),square(),square(4),square(7),square(),square(),square(1),square()],
                   [square(),square(),square(7),square(),square(),square(),square(),square(),square(2)],
                   [square(3),square(4),square(2),square(9),square(5),square(),square(),square(8),square()],
                   [square(),square(),square(6),square(),square(),square(),square(),square(4),square(3)],
                   [square(),square(),square(1),square(3),square(),square(4),square(),square(),square(7)],
                   [square(),square(7),square(3),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(1),square(),square(),square(),square(),square()],
                   [square(),square(3),square(),square(),square(),square(9),square(2),square(6),square()],
                   [square(2),square(),square(),square(),square(4),square(6),square(8),square(),square()]))

        solution_board = board(([square(5),square(6),square(8),square(4),square(7),square(2),square(3),square(1),square(9)],
                   [square(1),square(9),square(7),square(6),square(3),square(8),square(4),square(5),square(2)],
                   [square(3),square(4),square(2),square(9),square(5),square(1),square(7),square(8),square(6)],
                   [square(9),square(2),square(6),square(8),square(1),square(7),square(5),square(4),square(3)],
                   [square(8),square(5),square(1),square(3),square(9),square(4),square(6),square(2),square(7)],
                   [square(4),square(7),square(3),square(2),square(6),square(5),square(1),square(9),square(8)],
                   [square(6),square(8),square(5),square(1),square(2),square(3),square(9),square(7),square(4)],
                   [square(7),square(3),square(4),square(5),square(8),square(9),square(2),square(6),square(1)],
                   [square(2),square(1),square(9),square(7),square(4),square(6),square(8),square(3),square(5)]))
        medium_board.solve()
        self.assertEqual(medium_board.test_out_table(), solution_board.test_out_table(), "\n\nUnsolved Squares: " + str(medium_board.test_unsolved()))

    def test_medium_board_2(self):
        """Tests medium sudoku puzzle 2"""
        medium_board = board(([square(),square(),square(),square(),square(),square(9),square(),square(),square()],
                   [square(2),square(),square(),square(),square(3),square(8),square(),square(),square()],
                   [square(7),square(3),square(4),square(),square(),square(),square(5),square(9),square()],
                   [square(5),square(6),square(8),square(),square(1),square(),square(4),square(),square()],
                   [square(),square(),square(2),square(6),square(),square(),square(),square(),square()],
                   [square(1),square(9),square(7),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(6),square(),square(4),square(),square(),square(7),square(1)],
                   [square(),square(7),square(),square(),square(),square(),square(2),square(5),square()],
                   [square(8),square(),square(),square(7),square(2),square(),square(3),square(),square()]))

        solution_board = board(([square(6),square(8),square(5),square(4),square(7),square(9),square(1),square(3),square(2)],
                   [square(2),square(1),square(9),square(5),square(3),square(8),square(7),square(6),square(4)],
                   [square(7),square(3),square(4),square(1),square(6),square(2),square(5),square(9),square(8)],
                   [square(5),square(6),square(8),square(9),square(1),square(3),square(4),square(2),square(7)],
                   [square(3),square(4),square(2),square(6),square(8),square(7),square(9),square(1),square(5)],
                   [square(1),square(9),square(7),square(2),square(5),square(4),square(6),square(8),square(3)],
                   [square(9),square(2),square(6),square(3),square(4),square(5),square(8),square(7),square(1)],
                   [square(4),square(7),square(3),square(8),square(9),square(1),square(2),square(5),square(6)],
                   [square(8),square(5),square(1),square(7),square(2),square(6),square(3),square(4),square(9)]))
        medium_board.solve()
        self.assertEqual(medium_board.test_out_table(), solution_board.test_out_table(), "\n\nUnsolved Squares: " + str(medium_board.test_unsolved()))

    def test_medium_board_3(self):
        """Tests medium sudoku puzzle 3"""
        medium_board = board(([square(6),square(5),square(),square(),square(3),square(2),square(9),square(),square(4)],
                   [square(),square(4),square(),square(),square(),square(8),square(),square(),square()],
                   [square(),square(9),square(1),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(6),square(4),square(),square(),square(),square(1),square(9)],
                   [square(3),square(),square(),square(),square(),square(),square(),square(8),square()],
                   [square(),square(7),square(),square(),square(8),square(3),square(),square(),square(2)],
                   [square(),square(),square(),square(),square(7),square(),square(),square(4),square()],
                   [square(),square(),square(),square(),square(),square(6),square(1),square(),square()],
                   [square(),square(1),square(5),square(),square(4),square(),square(6),square(2),square()]))

        solution_board = board(([square(6),square(5),square(8),square(1),square(3),square(2),square(9),square(7),square(4)],
                   [square(7),square(4),square(3),square(5),square(9),square(8),square(2),square(6),square(1)],
                   [square(2),square(9),square(1),square(7),square(6),square(4),square(8),square(3),square(5)],
                   [square(5),square(8),square(6),square(4),square(2),square(7),square(3),square(1),square(9)],
                   [square(3),square(2),square(4),square(9),square(1),square(5),square(7),square(8),square(6)],
                   [square(1),square(7),square(9),square(6),square(8),square(3),square(4),square(5),square(2)],
                   [square(9),square(6),square(2),square(8),square(7),square(1),square(5),square(4),square(3)],
                   [square(4),square(3),square(7),square(2),square(5),square(6),square(1),square(9),square(8)],
                   [square(8),square(1),square(5),square(3),square(4),square(9),square(6),square(2),square(7)]))
        medium_board.solve()
        self.assertEqual(medium_board.test_out_table(), solution_board.test_out_table(), "\n\nUnsolved Squares: " + str(medium_board.test_unsolved()))

class Test_Hard_Sudoku(unittest.TestCase):
    """Tests multiple hard sudoku puzzles"""
    def test_hard_board_1(self):
        """Tests hard sudoku puzzle 1"""
        hard_board = board(([square(4),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(3),square(),square(8),square(),square(),square(),square(),square(),square()],
                   [square(),square(6),square(1),square(4),square(7),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(5),square(),square(2),square(7)],
                   [square(),square(),square(),square(),square(),square(),square(8),square(),square()],
                   [square(6),square(),square(3),square(),square(),square(),square(5),square(),square()],
                   [square(8),square(),square(),square(6),square(9),square(),square(1),square(),square(5)],
                   [square(),square(),square(),square(),square(1),square(2),square(),square(6),square(9)],
                   [square(1),square(),square(),square(3),square(),square(7),square(2),square(),square(8)]))

        solution_board = board(([square(4),square(2),square(9),square(5),square(8),square(1),square(7),square(3),square(6)],
                   [square(3),square(7),square(8),square(2),square(6),square(9),square(4),square(5),square(1)],
                   [square(5),square(6),square(1),square(4),square(7),square(3),square(9),square(8),square(2)],
                   [square(9),square(8),square(4),square(1),square(3),square(5),square(6),square(2),square(7)],
                   [square(2),square(5),square(7),square(9),square(4),square(6),square(8),square(1),square(3)],
                   [square(6),square(1),square(3),square(7),square(2),square(8),square(5),square(9),square(4)],
                   [square(8),square(3),square(2),square(6),square(9),square(4),square(1),square(7),square(5)],
                   [square(7),square(4),square(5),square(8),square(1),square(2),square(3),square(6),square(9)],
                   [square(1),square(9),square(6),square(3),square(5),square(7),square(2),square(4),square(8)]))
        hard_board.solve()
        self.assertEqual(hard_board.test_out_table(), solution_board.test_out_table(), "\n\nUnsolved Squares: " + str(hard_board.test_unsolved()))

    def test_hard_board_2(self):
        """Tests hard sudoku puzzle 2"""
        hard_board = board(([square(7),square(),square(),square(9),square(),square(),square(4),square(),square()],
                   [square(),square(),square(),square(),square(8),square(5),square(),square(),square()],
                   [square(),square(),square(1),square(),square(),square(),square(),square(2),square()],
                   [square(8),square(),square(4),square(),square(),square(),square(6),square(7),square(2)],
                   [square(5),square(),square(7),square(),square(4),square(),square(),square(),square()],
                   [square(),square(6),square(),square(8),square(2),square(),square(),square(),square()],
                   [square(3),square(),square(),square(4),square(9),square(),square(1),square(),square(7)],
                   [square(),square(),square(),square(),square(1),square(),square(),square(),square()],
                   [square(9),square(),square(),square(7),square(),square(),square(),square(8),square(4)]))

        solution_board = board(([square(7),square(3),square(8),square(9),square(6),square(2),square(4),square(1),square(5)],
                   [square(2),square(4),square(9),square(1),square(8),square(5),square(7),square(6),square(3)],
                   [square(6),square(5),square(1),square(3),square(7),square(4),square(9),square(2),square(8)],
                   [square(8),square(9),square(4),square(5),square(3),square(1),square(6),square(7),square(2)],
                   [square(5),square(2),square(7),square(6),square(4),square(9),square(8),square(3),square(1)],
                   [square(1),square(6),square(3),square(8),square(2),square(7),square(5),square(4),square(9)],
                   [square(3),square(8),square(2),square(4),square(9),square(6),square(1),square(5),square(7)],
                   [square(4),square(7),square(5),square(2),square(1),square(8),square(3),square(9),square(6)],
                   [square(9),square(1),square(6),square(7),square(5),square(3),square(2),square(8),square(4)]))
        hard_board.solve()
        self.assertEqual(hard_board.test_out_table(), solution_board.test_out_table(), "\n\nUnsolved Squares: " + str(hard_board.test_unsolved()))

class Test_Expert_Sudoku(unittest.TestCase):
    """Tests multiple expert sudoku puzzles"""
    def test_expert_board_1(self):
        """Tests expert sudoku puzzle 1"""
        expert_board = board(([square(),square(),square(6),square(),square(),square(2),square(),square(),square()],
                   [square(),square(8),square(),square(),square(),square(),square(),square(5),square(2)],
                   [square(),square(9),square(),square(),square(3),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(4),square(),square()],
                   [square(1),square(),square(4),square(),square(),square(),square(),square(),square(6)],
                   [square(3),square(),square(),square(),square(),square(9),square(1),square(),square()],
                   [square(),square(),square(),square(6),square(),square(),square(),square(7),square()],
                   [square(),square(),square(),square(1),square(4),square(3),square(),square(),square()],
                   [square(),square(),square(),square(9),square(),square(),square(8),square(6),square()]))

        solution_board = board(([square(5),square(1),square(6),square(8),square(9),square(2),square(7),square(4),square(3)],
                   [square(4),square(8),square(3),square(7),square(1),square(6),square(9),square(5),square(2)],
                   [square(7),square(9),square(2),square(5),square(3),square(4),square(6),square(1),square(8)],
                   [square(8),square(6),square(9),square(2),square(5),square(1),square(4),square(3),square(7)],
                   [square(1),square(5),square(4),square(3),square(8),square(7),square(2),square(9),square(6)],
                   [square(3),square(2),square(7),square(4),square(6),square(9),square(1),square(8),square(5)],
                   [square(9),square(4),square(5),square(6),square(2),square(8),square(3),square(7),square(1)],
                   [square(6),square(7),square(8),square(1),square(4),square(3),square(5),square(2),square(9)],
                   [square(2),square(3),square(1),square(9),square(7),square(5),square(8),square(6),square(4)]))
        expert_board.solve()
        self.assertEqual(expert_board.test_out_table(), solution_board.test_out_table(), "\n\nUnsolved Squares: " + str(expert_board.test_unsolved()))

    def test_expert_board_2(self):
        """Tests expert sudoku puzzle 2"""
        expert_board = board(([square(),square(),square(),square(),square(3),square(),square(),square(),square()],
                   [square(),square(),square(1),square(),square(7),square(6),square(9),square(4),square()],
                   [square(),square(8),square(),square(9),square(),square(),square(),square(),square()],
                   [square(),square(4),square(),square(),square(),square(1),square(),square(),square()],
                   [square(),square(2),square(8),square(),square(9),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(1),square(6),square()],
                   [square(7),square(),square(),square(8),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(),square(4),square(),square(2)],
                   [square(),square(9),square(),square(),square(1),square(),square(3),square(),square()]))

        solution_board = board(([square(4),square(6),square(9),square(1),square(3),square(8),square(2),square(7),square(5)],
                   [square(3),square(5),square(1),square(2),square(7),square(6),square(9),square(4),square(8)],
                   [square(2),square(8),square(7),square(9),square(4),square(5),square(6),square(3),square(1)],
                   [square(9),square(4),square(6),square(7),square(5),square(1),square(8),square(2),square(3)],
                   [square(1),square(2),square(8),square(6),square(9),square(3),square(7),square(5),square(4)],
                   [square(5),square(7),square(3),square(4),square(8),square(2),square(1),square(6),square(9)],
                   [square(7),square(3),square(4),square(8),square(2),square(9),square(5),square(1),square(6)],
                   [square(8),square(1),square(5),square(3),square(6),square(7),square(4),square(9),square(2)],
                   [square(6),square(9),square(2),square(5),square(1),square(4),square(3),square(8),square(7)]))
        expert_board.solve()
        self.assertEqual(expert_board.test_out_table(), solution_board.test_out_table(), "\n\nUnsolved Squares: " + str(expert_board.test_unsolved()))

class Test_Evil_Sudoku(unittest.TestCase):
    """Tests multiple evil sudoku puzzles"""
    def test_evil_board_1(self):
        """Tests evil sudoku puzzle 1"""
        evil_board = board(([square(),square(),square(),square(4),square(),square(),square(1),square(),square()],
                   [square(6),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(2),square(5),square(),square(),square(7),square(),square(),square(4),square()],
                   [square(),square(),square(9),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(3),square(),square(),square(8)],
                   [square(4),square(7),square(),square(),square(2),square(),square(),square(1),square()],
                   [square(),square(),square(1),square(),square(9),square(),square(),square(),square()],
                   [square(5),square(9),square(),square(),square(),square(2),square(3),square(),square()],
                   [square(),square(),square(6),square(),square(),square(),square(),square(5),square()]))

        solution_board = board(([square(9),square(8),square(7),square(4),square(5),square(6),square(1),square(3),square(2)],
                   [square(6),square(1),square(4),square(2),square(3),square(8),square(5),square(7),square(9)],
                   [square(2),square(5),square(3),square(9),square(7),square(1),square(8),square(4),square(6)],
                   [square(8),square(3),square(9),square(1),square(6),square(7),square(4),square(2),square(5)],
                   [square(1),square(6),square(2),square(5),square(4),square(3),square(7),square(9),square(8)],
                   [square(4),square(7),square(5),square(8),square(2),square(9),square(6),square(1),square(3)],
                   [square(3),square(4),square(1),square(6),square(9),square(5),square(2),square(8),square(7)],
                   [square(5),square(9),square(8),square(7),square(1),square(2),square(3),square(6),square(4)],
                   [square(7),square(2),square(6),square(3),square(8),square(4),square(9),square(5),square(1)]))
        evil_board.solve()
        self.assertEqual(evil_board.test_out_table(),solution_board.test_out_table(), "\n\nUnsolved Squares: " + str(evil_board.test_unsolved()))

    def test_evil_board_2(self):
        """Tests evil sudoku puzzle 2"""
        evil_board = board(([square(9),square(),square(),square(),square(5),square(),square(),square(),square()],
                   [square(),square(3),square(5),square(),square(),square(2),square(),square(),square(7)],
                   [square(8),square(),square(),square(),square(),square(),square(3),square(),square()],
                   [square(),square(),square(9),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(),square(8),square(),square(4),square()],
                   [square(),square(5),square(7),square(),square(4),square(),square(6),square(),square()],
                   [square(),square(),square(),square(1),square(),square(),square(),square(),square(2)],
                   [square(),square(6),square(4),square(),square(8),square(),square(7),square(),square()],
                   [square(3),square(),square(),square(),square(),square(),square(),square(),square()]))

        solution_board = board(([square(9),square(7),square(6),square(8),square(5),square(3),square(1),square(2),square(4)],
                   [square(1),square(3),square(5),square(4),square(9),square(2),square(8),square(6),square(7)],
                   [square(8),square(4),square(2),square(6),square(1),square(7),square(3),square(9),square(5)],
                   [square(4),square(8),square(9),square(3),square(6),square(5),square(2),square(7),square(1)],
                   [square(6),square(1),square(3),square(7),square(2),square(8),square(5),square(4),square(9)],
                   [square(2),square(5),square(7),square(9),square(4),square(1),square(6),square(3),square(8)],
                   [square(7),square(9),square(8),square(1),square(3),square(6),square(4),square(5),square(2)],
                   [square(5),square(6),square(4),square(2),square(8),square(9),square(7),square(1),square(3)],
                   [square(3),square(2),square(1),square(5),square(7),square(4),square(9),square(8),square(6)]))
        evil_board.solve()
        self.assertEqual(evil_board.test_out_table(),solution_board.test_out_table(), "\n\nUnsolved Squares: " + str(evil_board.test_unsolved()))

if __name__== '__main__':
    unittest.main()
