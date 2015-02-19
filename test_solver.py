__author__ = 'Tirth'

import unittest
import solver


class TestSolver(unittest.TestCase):
    def setUp(self):
        self.puzzle = solver.Sudoku()

        # incomplete easy (record: 4 iters)
        easy_sudoku = [i for i in range(9)]
        easy_sudoku[0] = [8, 3, 0, 0, 7, 6, 0, 4, 2]
        easy_sudoku[1] = [6, 0, 0, 3, 0, 0, 0, 9, 7]
        easy_sudoku[2] = [0, 0, 0, 0, 8, 2, 1, 0, 0]
        easy_sudoku[3] = [0, 9, 0, 0, 3, 0, 0, 0, 5]
        easy_sudoku[4] = [0, 2, 6, 0, 0, 0, 7, 3, 0]
        easy_sudoku[5] = [3, 0, 0, 0, 2, 0, 0, 1, 0]
        easy_sudoku[6] = [0, 0, 3, 4, 6, 0, 0, 0, 0]
        easy_sudoku[7] = [1, 7, 0, 0, 0, 3, 0, 0, 6]
        easy_sudoku[8] = [2, 6, 0, 7, 9, 0, 0, 5, 4]

        # incomplete hard
        hard_sudoku = [i for i in range(9)]
        hard_sudoku[0] = [0, 0, 3, 1, 0, 5, 0, 6, 0]
        hard_sudoku[1] = [0, 0, 0, 0, 0, 4, 0, 0, 8]
        hard_sudoku[2] = [0, 6, 0, 0, 0, 0, 5, 0, 7]
        hard_sudoku[3] = [0, 5, 6, 0, 0, 0, 0, 0, 0]
        hard_sudoku[4] = [0, 9, 4, 6, 0, 2, 1, 5, 0]
        hard_sudoku[5] = [0, 0, 0, 0, 0, 0, 6, 2, 0]
        hard_sudoku[6] = [5, 0, 9, 0, 0, 0, 0, 4, 0]
        hard_sudoku[7] = [6, 0, 0, 4, 0, 0, 0, 0, 0]
        hard_sudoku[8] = [0, 4, 0, 2, 0, 3, 9, 0, 0]

        # complete
        done_sudoku = [i for i in range(9)]
        done_sudoku[0] = [3, 9, 1, 2, 8, 6, 5, 7, 4]
        done_sudoku[1] = [4, 8, 7, 3, 5, 9, 1, 2, 6]
        done_sudoku[2] = [6, 5, 2, 7, 1, 4, 8, 3, 9]
        done_sudoku[3] = [8, 7, 5, 4, 3, 1, 6, 9, 2]
        done_sudoku[4] = [2, 1, 3, 9, 6, 7, 4, 8, 5]
        done_sudoku[5] = [9, 6, 4, 5, 2, 8, 7, 1, 3]
        done_sudoku[6] = [1, 4, 9, 6, 7, 3, 2, 5, 8]
        done_sudoku[7] = [5, 3, 8, 1, 4, 2, 9, 6, 7]
        done_sudoku[8] = [7, 2, 6, 8, 9, 5, 3, 4, 1]

        self.puzzle.get_input(hard_sudoku)  # change puzzles here

    def test_solve(self):
        print(self.puzzle)
        self.puzzle.solve()
        self.assertTrue(self.puzzle.valid_puzzle())


if __name__ == '__main__':
    unittest.main(exit=False)