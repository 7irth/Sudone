__author__ = 'Tirth Patel <complaints@tirthpatel.com>'

import unittest
import solver


class TestSolver(unittest.TestCase):
    def setUp(self):
        self.puzzle = solver.Sudoku()

        # easy (record: 4 iters)
        self.easy = [i for i in range(9)]
        self.easy[0] = [8, 3, 0, 0, 7, 6, 0, 4, 2]
        self.easy[1] = [6, 0, 0, 3, 0, 0, 0, 9, 7]
        self.easy[2] = [0, 0, 0, 0, 8, 2, 1, 0, 0]
        self.easy[3] = [0, 9, 0, 0, 3, 0, 0, 0, 5]
        self.easy[4] = [0, 2, 6, 0, 0, 0, 7, 3, 0]
        self.easy[5] = [3, 0, 0, 0, 2, 0, 0, 1, 0]
        self.easy[6] = [0, 0, 3, 4, 6, 0, 0, 0, 0]
        self.easy[7] = [1, 7, 0, 0, 0, 3, 0, 0, 6]
        self.easy[8] = [2, 6, 0, 7, 9, 0, 0, 5, 4]

        # medium
        self.medium = [i for i in range(9)]
        self.medium[0] = [0, 5, 0, 0, 0, 0, 0, 0, 6]
        self.medium[1] = [4, 8, 0, 0, 9, 0, 0, 0, 3]
        self.medium[2] = [9, 0, 3, 8, 0, 0, 0, 0, 0]
        self.medium[3] = [0, 1, 7, 0, 0, 4, 0, 0, 0]
        self.medium[4] = [6, 0, 0, 1, 7, 2, 0, 0, 5]
        self.medium[5] = [0, 0, 0, 5, 0, 0, 8, 1, 0]
        self.medium[6] = [0, 0, 0, 0, 0, 3, 5, 0, 8]
        self.medium[7] = [7, 0, 0, 0, 5, 0, 0, 4, 1]
        self.medium[8] = [8, 0, 0, 0, 0, 0, 0, 9, 0]

        # hard
        self.hard = [i for i in range(9)]
        self.hard[0] = [0, 0, 3, 1, 0, 5, 0, 6, 0]
        self.hard[1] = [0, 0, 0, 0, 0, 4, 0, 0, 8]
        self.hard[2] = [0, 6, 0, 0, 0, 0, 5, 0, 7]
        self.hard[3] = [0, 5, 6, 0, 0, 0, 0, 0, 0]
        self.hard[4] = [0, 9, 4, 6, 0, 2, 1, 5, 0]
        self.hard[5] = [0, 0, 0, 0, 0, 0, 6, 2, 0]
        self.hard[6] = [5, 0, 9, 0, 0, 0, 0, 4, 0]
        self.hard[7] = [6, 0, 0, 4, 0, 0, 0, 0, 0]
        self.hard[8] = [0, 4, 0, 2, 0, 3, 9, 0, 0]

        # evil
        self.evil = [i for i in range(9)]
        self.evil[0] = [0, 0, 5, 0, 9, 0, 4, 0, 0]
        self.evil[1] = [7, 0, 0, 0, 4, 6, 0, 0, 0]
        self.evil[2] = [0, 0, 0, 3, 0, 0, 0, 9, 0]
        self.evil[3] = [6, 0, 0, 0, 0, 0, 0, 2, 0]
        self.evil[4] = [0, 9, 0, 1, 5, 8, 0, 3, 0]
        self.evil[5] = [0, 8, 0, 0, 0, 0, 0, 0, 9]
        self.evil[6] = [0, 6, 0, 0, 0, 5, 0, 0, 0]
        self.evil[7] = [0, 0, 0, 9, 2, 0, 0, 0, 1]
        self.evil[8] = [0, 0, 8, 0, 1, 0, 9, 0, 0]

        # complete
        self.done = [i for i in range(9)]
        self.done[0] = [3, 9, 1, 2, 8, 6, 5, 7, 4]
        self.done[1] = [4, 8, 7, 3, 5, 9, 1, 2, 6]
        self.done[2] = [6, 5, 2, 7, 1, 4, 8, 3, 9]
        self.done[3] = [8, 7, 5, 4, 3, 1, 6, 9, 2]
        self.done[4] = [2, 1, 3, 9, 6, 7, 4, 8, 5]
        self.done[5] = [9, 6, 4, 5, 2, 8, 7, 1, 3]
        self.done[6] = [1, 4, 9, 6, 7, 3, 2, 5, 8]
        self.done[7] = [5, 3, 8, 1, 4, 2, 9, 6, 7]
        self.done[8] = [7, 2, 6, 8, 9, 5, 3, 4, 1]

    def test_solve(self):
        self.puzzle.get_input(self.easy)  # choose puzzle
        # print(self.puzzle)

        self.assertTrue(self.puzzle.solve())

if __name__ == '__main__':
    unittest.main(exit=False)