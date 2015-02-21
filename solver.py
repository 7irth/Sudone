__author__ = 'Tirth Patel <complaints@tirthpatel.com>'


class Sudoku:
    def __init__(self, size=9, max_iterations=25):
        self.sudoku = [[0 for _ in range(size)] for _ in range(size)]
        self.empties = {}
        self.box_empties = {}
        self.current = 0
        self.max_iter = max_iterations
        self.spots = len(self.sudoku) ** 2

    def get_input(self, puzzle=None):
        if puzzle:
            for row in range(len(self.sudoku)):
                count = row * len(self.sudoku)
                for cell in range(len(self.sudoku)):
                    self.sudoku[row][cell] = int(puzzle[count + cell])
        else:
            print('Enter numbers left to right, row by row, top to bottom, '
                  'no spaces, 0 for blank: ')

            for row in range(len(self.sudoku)):
                row = input('Row ' + str(row) + ': ')

                for cell in range(len(self.sudoku)):
                    self.sudoku[row][cell] = int(row[cell])

        return self.valid_puzzle(initial=True)

    def valid_puzzle(self, initial=False):
        rows, cells, boxes = self.get_stuff()
        rows_cells_boxes = rows + cells + boxes

        if not initial:  # check for complete puzzle
            for thing in rows_cells_boxes:
                if sorted(thing) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                    # print('NOPE', thing, rows_cells_boxes.index(thing))
                    return False

        else:  # make sure it's valid to start, possible without solution?

            self.fill_empties()
            for empty in self.empties.keys():
                if len(self.empties[empty][3]) == 0:
                    print('Invalid puzzle')
                    return False

            for thing in rows_cells_boxes:
                for number in thing:  # numbers not repeated and in range
                    if number != 0 and not (thing.count(number) == 1
                                            and (1 <= number <= 9)):
                        print('Invalid puzzle')
                        return False

        return True

    def get_stuff(self):
        rows, cells, boxes = [], [], []

        for i in range(len(self.sudoku)):
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

        s += 'after ' + str(self.current) + ' iterations, ' \
             + str(len(self.empties)) + ' empty spots remain\n'
        return s

    @staticmethod
    def get_box(coordinates):
        row = coordinates[0]
        cell = coordinates[1]

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

        return box

    def fill_empties(self):
        self.empties = {}
        rows, cells, boxes = self.get_stuff()

        for row in range(len(self.sudoku)):
            for cell in range(len(self.sudoku[row])):
                if self.sudoku[row][cell] == 0:  # go through empty cells

                    # determine box, uggo again
                    box = self.get_box((row, cell))

                    possibilities = [i for i in range(1, 10) if i not in
                                     (rows[row] + cells[cell] + boxes[box])]

                    # print(row, cell)
                    # print('--')
                    # print('row', rows[row])  # your boat
                    # print('col', cells[cell])
                    # print('box', boxes[box])
                    # print('pos', possibilities)
                    # print()

                    self.empties[(row, cell)] = \
                        [rows[row], cells[cell], boxes[box], possibilities]

    def check_cells(self):
        for cell in self.empties.keys():

            # only one possibility, put it in the puzzle
            if len(self.empties[cell][3]) == 1:
                self.sudoku[cell[0]][cell[1]] = self.empties[cell][3].pop()
                self.fill_empties()

                print(cell, self.sudoku[cell[0]][cell[1]], 'by cells')

    def check_boxes(self):
        self.box_empties = {}

        for cell in self.empties.keys():

            # enumerate possibilities per box
            box = self.get_box(cell)

            if box in self.box_empties.keys():
                self.box_empties[box].append(cell)
                self.box_empties[box].append(self.empties[cell][3])
            else:
                self.box_empties[box] = [cell, self.empties[cell][3]]

        # each box with empty cells
        for vacant in self.box_empties.keys():
            current = self.box_empties[vacant]  # empty cells in box

            counts = {}

            # figure out how many times each possibility shows up in box
            for possibilities in current:
                if type(possibilities) is list:  # exclude coordinates
                    for each in possibilities:
                        if each in counts.keys():
                            counts[each] += 1
                        else:
                            counts[each] = 1

            for key in counts.keys():
                if counts[key] == 1:  # only showed up once, put in puzzle
                    for cell in current:
                        if type(cell) is list and key in cell:
                            coords = current[current.index(cell) - 1]
                            self.sudoku[coords[0]][coords[1]] = key
                            self.fill_empties()

                            print(coords, key, 'by boxes')

    def rando(self):
        smallest = 9
        for cell in self.empties.keys():
            if len(self.empties[cell][3]) < smallest:
                smallest = len(self.empties[cell][3])

        for cell in self.empties.keys():
            if len(self.empties[cell][3]) == smallest:
                print('stuff', self.empties[cell][3])

    def solve(self):  # where the magic happens
        print('NOW AT', self.current)
        print(self.__str__())

        if self.spots > len(self.empties) > 0 and self.current < self.max_iter:
            self.spots = len(self.empties)
            self.current += 1

            print('--- added ---')
            # check by cells
            self.check_cells()

            # check by boxes
            self.check_boxes()
            print('---\n')

            # recurse until solved
            return self.solve()
        elif len(self.empties) > 0 and self.current < self.max_iter:
            self.spots = len(self.empties)
            self.current += 1
            self.rando()
            return self.solve()
        else:
            if self.valid_puzzle():
                return True
            else:
                self.print_empties()
                return False

    def print_empties(self):
        for cell in sorted(self.empties.keys(), key=self.get_box):
            print(cell, self.get_box(cell), self.empties[cell][3])

if __name__ == '__main__':
    sudoku = Sudoku()
    if sudoku.get_input():
        if sudoku.solve():
            print(sudoku)
            print('YAY')