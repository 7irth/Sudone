__author__ = 'tirth'


class Sudoku:
    def __init__(self, size=9):
        self.size = size
        self.sudoku = [[0 for i in range(self.size)] for j in range(self.size)]

    def __str__(self):
        s = ""
        col_counter, row_counter = 0, 0

        for row in self.sudoku:
            for column in row:

                if col_counter == 3 or col_counter == 6:
                    s += '| '
                col_counter += 1
                s += str(column) + ' '

            s += '\n'

            row_counter += 1

            if row_counter == 3 or row_counter == 6:
                s += "------|-------|------\n"

            col_counter = 0

        return s


if __name__ == '__main__':
    sudoku = Sudoku()
    print(sudoku)