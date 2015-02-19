__author__ = 'Tirth Patel <complaints@tirthpatel.com>'

import unittest
import solver


class TestSolver(unittest.TestCase):
    def setUp(self):
        self.puzzle = solver.Sudoku()

        # easy (record: 4 iters)
        self.easy = '830076042' \
                    '600300097' \
                    '000082100' \
                    '090030005' \
                    '026000730' \
                    '300020010' \
                    '003460000' \
                    '170003006' \
                    '260790054'

        # medium
        self.medium = '050000006' \
                      '480090003' \
                      '903800000' \
                      '017004000' \
                      '600172005' \
                      '000500810' \
                      '000003508' \
                      '700050041' \
                      '800000090'  # (0, 0) -> 2 to make solvable

        # hard
        self.hard = '003105060' \
                    '000004008' \
                    '060000507' \
                    '056000000' \
                    '094602150' \
                    '000000620' \
                    '509000040' \
                    '600400000' \
                    '040203900'

        # evil
        self.evil = '005090400' \
                    '700046000' \
                    '000300090' \
                    '600000020' \
                    '090158030' \
                    '080000009' \
                    '060005000' \
                    '000920001' \
                    '008010900'

        # complete
        self.done = '391286574' \
                    '487359126' \
                    '652714839' \
                    '875431692' \
                    '213967485' \
                    '964528713' \
                    '149673258' \
                    '538142967' \
                    '726895341'

    def test_solve(self):
        x_wing = '005004000000060090300000007000040000008000400' \
                 '541000009200000003007400000000003000'

        if self.puzzle.get_input(self.medium):  # choose puzzle
            self.assertTrue(self.puzzle.solve())

if __name__ == '__main__':
    unittest.main(exit=False)