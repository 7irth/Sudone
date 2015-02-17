__author__ = 'tirth'


class Sudoku:
    def __init__(self, size=9):
        self.size = size
        self.sudoku = [[0 for i in range(self.size)] for j in range(self.size)]

    def get_input(self):
        # print('Enter numbers left to right, row by row, top to bottom, '
        #       'no spaces, 0 for blank: ')
        #
        # for i in range(self.size-8):
        #     row = input('Row ' + str(i) + ': ')
        #
        #     for j in range(self.size):
        #         self.sudoku[i][j] = row[j]

        # for testing
        self.sudoku[0] = [8, 3, 0, 0, 7, 6, 0, 4, 2]
        self.sudoku[1] = [6, 0, 0, 3, 0, 0, 0, 9, 7]
        self.sudoku[2] = [0, 0, 0, 0, 8, 2, 1, 0, 0]
        self.sudoku[3] = [0, 9, 0, 0, 3, 0, 0, 0, 5]
        self.sudoku[4] = [0, 2, 6, 0, 0, 0, 7, 3, 0]
        self.sudoku[5] = [3, 0, 0, 0, 2, 0, 0, 1, 0]
        self.sudoku[6] = [0, 0, 3, 4, 6, 0, 0, 0, 0]
        self.sudoku[7] = [1, 7, 0, 0, 0, 3, 0, 0, 6]
        self.sudoku[8] = [2, 6, 0, 7, 9, 0, 0, 5, 4]

    def __str__(self):
        s = ""
        col_counter, row_counter = 0, 0

        for row in self.sudoku:
            for column in row:

                if col_counter == 3 or col_counter == 6:
                    s += '| '
                col_counter += 1

                if column != 0:
                    s += str(column) + ' '
                else:
                    s += '  '

            s += '\n'

            row_counter += 1

            if row_counter == 3 or row_counter == 6:
                s += "------|-------|------\n"

            col_counter = 0

        return s


if __name__ == '__main__':
    sudoku = Sudoku()
    sudoku.get_input()
    print(sudoku)