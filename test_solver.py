__author__ = 'Tirth Patel <complaints@tirthpatel.com>'

import unittest
import solver
import time


class TestSolver(unittest.TestCase):
    def setUp(self):
        self.sudoku = solver.Sudoku(max_iterations=1000, debug_print=False)

        # (record: 4 iters)
        easy = '830076042' \
               '600300097' \
               '000082100' \
               '090030005' \
               '026000730' \
               '300020010' \
               '003460000' \
               '170003006' \
               '260790054'

        # (random record: 8 iters, average ~13 iters [sorted]
        #                 7 iters, average ~22 iters [random])
        medium = '050000006' \
                 '480090003' \
                 '903800000' \
                 '017004000' \
                 '600172005' \
                 '000500810' \
                 '000003508' \
                 '700050041' \
                 '800000090'

        # hard record: 18 iters (14.55ms), average ~38 iters (31.9ms)
        #
        # after 100 [sorted] runs
        # min iters: 19, max iters: 153
        # min time:  14.6, max time: 127.76
        # average iters: 42.68
        # average time:  35.17
        #
        # after 100 [unsorted] runs
        # min iters: 19, max iters: 100
        # min time:  14.55, max time: 119.27
        # average iters: 37.84
        # average time:  31.9
        #
        # after 100 [random] runs
        # min iters: 18, max iters: 365
        # min time:  14.69, max time: 301.51
        # average iters: 96.8
        # average time:  82.78
        hard = '003105060' \
               '000004008' \
               '060000507' \
               '056000000' \
               '094602150' \
               '000000620' \
               '509000040' \
               '600400000' \
               '040203900'

        # (random record: 17 iters, average ~130 iters [sorted]
        #                 17 iters, average ~115 iters [unsorted]
        #                 13 iters, average ~128 iters [random])
        evil = '005090400' \
               '700046000' \
               '000300090' \
               '600000020' \
               '090158030' \
               '080000009' \
               '060005000' \
               '000920001' \
               '008010900'

        # complete
        done = '391286574' \
               '487359126' \
               '652714839' \
               '875431692' \
               '213967485' \
               '964528713' \
               '149673258' \
               '538142967' \
               '726895341'

        # supposedly the world's hardest?
        everest = '800000000' \
                  '003600000' \
                  '070090200' \
                  '050007000' \
                  '000045700' \
                  '000100030' \
                  '001000068' \
                  '008500010' \
                  '090000400'

        self.puzzle = hard  # choose puzzle

    def test_solve(self):
        if self.sudoku.get_input(self.puzzle):
            self.assertTrue(self.sudoku.solve())
            # print('denied', self.sudoku.removal)
            print('done in', self.sudoku.current)

    def test_efficiency(self):
        iterations, times = [], []
        validity = 100

        for i in range(validity):
            if self.sudoku.get_input(self.puzzle):
                start = time.clock()
                self.assertTrue(self.sudoku.solve())
                end = time.clock()

                times.append(end - start)

            progress = i/(validity/100)
            if progress % 10.0 == 0.0:
                print(str(progress) + "%")

            iterations.append(self.sudoku.current)

            self.sudoku = solver.Sudoku(max_iterations=1000)
            self.sudoku.get_input(self.puzzle)

        print('--')
        print('after', len(iterations), 'runs')
        print('min iters:', str(min(iterations)) + ',',
              'max iters:', max(iterations))
        print('min time: ', str(round(min(times) * 1000, 2)) + ',',
              'max time:', round(max(times) * 1000, 2))
        print('average iters:', sum(iterations)/len(iterations))
        print('average time: ', round((sum(times)/len(times) * 1000), 2))


if __name__ == '__main__':
    unittest.main(exit=False)