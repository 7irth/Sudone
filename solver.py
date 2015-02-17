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
        # incomplete
        self.sudoku[0] = [8, 3, 0, 0, 7, 6, 0, 4, 2]
        self.sudoku[1] = [6, 0, 0, 3, 0, 0, 0, 9, 7]
        self.sudoku[2] = [0, 0, 0, 0, 8, 2, 1, 0, 0]
        self.sudoku[3] = [0, 9, 0, 0, 3, 0, 0, 0, 5]
        self.sudoku[4] = [0, 2, 6, 0, 0, 0, 7, 3, 0]
        self.sudoku[5] = [3, 0, 0, 0, 2, 0, 0, 1, 0]
        self.sudoku[6] = [0, 0, 3, 4, 6, 0, 0, 0, 0]
        self.sudoku[7] = [1, 7, 0, 0, 0, 3, 0, 0, 6]
        self.sudoku[8] = [2, 6, 0, 7, 9, 0, 0, 5, 4]

        # complete
        self.sudoku[0] = [3, 9, 1, 2, 8, 6, 5, 7, 4]
        self.sudoku[1] = [4, 8, 7, 3, 5, 9, 1, 2, 6]
        self.sudoku[2] = [6, 5, 2, 7, 1, 4, 8, 3, 9]
        self.sudoku[3] = [8, 7, 5, 4, 3, 1, 6, 9, 2]
        self.sudoku[4] = [2, 1, 3, 9, 6, 7, 4, 8, 5]
        self.sudoku[5] = [9, 6, 4, 5, 2, 8, 7, 1, 3]
        self.sudoku[6] = [1, 4, 9, 6, 7, 3, 2, 5, 8]
        self.sudoku[7] = [5, 3, 8, 1, 4, 2, 9, 6, 7]
        self.sudoku[8] = [7, 2, 6, 8, 9, 5, 3, 4, 1]

    def check_puzzle(self):
        rows, cols, boxes = self.get_stuff()
        things_to_check = rows + cols + boxes

        for thing in things_to_check:
            if sorted(thing) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                return False
        return True

    def get_stuff(self):
        rows, cols, boxes = [], [], []

        for i in range(self.size):
            cols.append([])
            boxes.append([])

        for row in self.sudoku:
            rows.append(row)

            for i in range(len(row)):
                cols[i].append(row[i])

        # uggo
        for i in range(0, 3):
            boxes[0].extend(rows[i][0:3])
            boxes[1].extend(rows[i][3:6])
            boxes[2].extend(rows[i][6:9])

        for i in range(3, 6):
            boxes[3].extend(rows[i][0:3])
            boxes[4].extend(rows[i][3:6])
            boxes[5].extend(rows[i][6:9])

        for i in range(6, 9):
            boxes[6].extend(rows[i][0:3])
            boxes[7].extend(rows[i][3:6])
            boxes[8].extend(rows[i][6:9])

        return rows, cols, boxes

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
    print(sudoku.check_puzzle())