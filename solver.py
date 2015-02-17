__author__ = 'tirth'


class Sudoku:
    def __init__(self, size=9):
        self.size = size
        self.sudoku = [[0 for i in range(self.size)] for j in range(self.size)]

    def get_input(self):
        # print('Enter numbers left to right, row by row, top to bottom, '
        #       'no spaces, 0 for blank: ')
        #
        # for i in range(self.size):
        #     row = input('Row ' + str(i) + ': ')
        #
        #     for j in range(self.size):
        #         self.sudoku[i][j] = int(row[j])

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
        # self.sudoku[0] = [3, 9, 1, 2, 8, 6, 5, 7, 4]
        # self.sudoku[1] = [4, 8, 7, 3, 5, 9, 1, 2, 6]
        # self.sudoku[2] = [6, 5, 2, 7, 1, 4, 8, 3, 9]
        # self.sudoku[3] = [8, 7, 5, 4, 3, 1, 6, 9, 2]
        # self.sudoku[4] = [2, 1, 3, 9, 6, 7, 4, 8, 5]
        # self.sudoku[5] = [9, 6, 4, 5, 2, 8, 7, 1, 3]
        # self.sudoku[6] = [1, 4, 9, 6, 7, 3, 2, 5, 8]
        # self.sudoku[7] = [5, 3, 8, 1, 4, 2, 9, 6, 7]
        # self.sudoku[8] = [7, 2, 6, 8, 9, 5, 3, 4, 1]

        return self.check_puzzle(initial=True)

    def check_puzzle(self, initial=False):
        rows, cells, boxes = self.get_stuff()
        things_to_check = rows + cells + boxes

        if not initial:  # check for complete puzzle
            for thing in things_to_check:
                if sorted(thing) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                    print('NOPE', thing, things_to_check.index(thing))
                    return False
        else:
            for thing in things_to_check:
                for number in thing:  # numbers not repeated and in range
                    if number != 0 and not (thing.count(number) == 1
                                            and (1 <= number <= 9)):
                        return False

        return True

    def get_stuff(self):
        rows, cells, boxes = [], [], []

        for i in range(self.size):
            cells.append([])
            boxes.append([])

        for row in self.sudoku:
            rows.append(row)

            for i in range(len(row)):
                cells[i].append(row[i])

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

        return rows, cells, boxes

    def __str__(self):
        s = ""
        cell_counter, row_counter = 0, 0

        for row in self.sudoku:
            for cell in row:

                if cell_counter == 3 or cell_counter == 6:
                    s += '| '
                cell_counter += 1

                if cell != 0:
                    s += str(cell) + ' '
                else:
                    s += '  '

            s += '\n'

            row_counter += 1

            if row_counter == 3 or row_counter == 6:
                s += "------|-------|------\n"

            cell_counter = 0

        return s

    def get_empties(self):
        rows, cells, boxes = self.get_stuff()
        empties = {}

        for row in range(len(self.sudoku)):
            for cell in range(len(self.sudoku[row])):
                if self.sudoku[row][cell] == 0:  # go through empty cells
                    # print(row, cell)
                    # print('--')
                    # print('row', rows[row])  # your boat
                    # print('col', cells[cell])

                    # uggo again
                    if row < 3:
                        if cell < 3:
                            box = 0
                        elif cell > 5:
                            box = 2
                        else:
                            box = 1
                    elif row > 5:
                        if cell < 3:
                            box = 6
                        elif cell > 5:
                            box = 8
                        else:
                            box = 7
                    else:
                        if cell < 3:
                            box = 3
                        elif cell > 5:
                            box = 5
                        else:
                            box = 4

                    # print('box', boxes[box])
                    # print()

                    empties[(row, cell)] = [rows[row], cells[cell], boxes[box]]

        return empties

    def solve(self, empties):
        if len(empties) > 0:
            print('THINGS LEFT', len(empties))
            empty_cells = []

            for key in empties.keys():
                empty_cells.append(key)

            for empty in empty_cells:
                possibilities = []
                current = empties[empty]
                print(empty, current)

                if len(current) == 3:
                    for guess in range(1, 10):
                        if guess not in (current[0] + current[1] + current[2]):
                            possibilities.append(guess)
                    empties[empty].append(possibilities)
                    print(current)
                else:
                    for possibility in possibilities:
                        if possibility in (current[0] + current[1] + current[2]):
                            possibilities.remove(possibility)

                print(current[3])

                if len(current[3]) == 1:
                    self.sudoku[empty[0]][empty[1]] = possibilities.pop()
                    empties.pop(empty)

            self.solve(self.get_empties())  # TODO: optimize


if __name__ == '__main__':
    sudoku = Sudoku()
    if sudoku.get_input():
        print(sudoku)
        stuff = sudoku.get_empties()
        sudoku.solve(stuff)
        print(sudoku)