__author__ = 'tirth'


class Sudoku:
    def __init__(self, size=9, max_iterations=25):
        self.size = size
        self.sudoku = [[0 for i in range(self.size)] for j in range(self.size)]
        self.empties = {}
        self.box_empties = {}
        self.current_iteration = 0
        self.max_iterations = max_iterations

    def get_input(self):
        # print('Enter numbers left to right, row by row, top to bottom, '
        # 'no spaces, 0 for blank: ')
        #
        # for i in range(self.size):
        #     row = input('Row ' + str(i) + ': ')
        #
        #     for j in range(self.size):
        #         self.sudoku[i][j] = int(row[j])

        # for testing
        # incomplete easy (record: 4 iters)
        self.sudoku[0] = [8, 3, 0, 0, 7, 6, 0, 4, 2]
        self.sudoku[1] = [6, 0, 0, 3, 0, 0, 0, 9, 7]
        self.sudoku[2] = [0, 0, 0, 0, 8, 2, 1, 0, 0]
        self.sudoku[3] = [0, 9, 0, 0, 3, 0, 0, 0, 5]
        self.sudoku[4] = [0, 2, 6, 0, 0, 0, 7, 3, 0]
        self.sudoku[5] = [3, 0, 0, 0, 2, 0, 0, 1, 0]
        self.sudoku[6] = [0, 0, 3, 4, 6, 0, 0, 0, 0]
        self.sudoku[7] = [1, 7, 0, 0, 0, 3, 0, 0, 6]
        self.sudoku[8] = [2, 6, 0, 7, 9, 0, 0, 5, 4]

        # incomplete hard
        # self.sudoku[0] = [0, 0, 3, 1, 0, 5, 0, 6, 0]
        # self.sudoku[1] = [0, 0, 0, 0, 0, 4, 0, 0, 8]
        # self.sudoku[2] = [0, 6, 0, 0, 0, 0, 5, 0, 7]
        # self.sudoku[3] = [0, 5, 6, 0, 0, 0, 0, 0, 0]
        # self.sudoku[4] = [0, 9, 4, 6, 0, 2, 1, 5, 0]
        # self.sudoku[5] = [0, 0, 0, 0, 0, 0, 6, 2, 0]
        # self.sudoku[6] = [5, 0, 9, 0, 0, 0, 0, 4, 0]
        # self.sudoku[7] = [6, 0, 0, 4, 0, 0, 0, 0, 0]
        # self.sudoku[8] = [0, 4, 0, 2, 0, 3, 9, 0, 0]

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
        rows_cells_boxes = rows + cells + boxes

        if not initial:  # check for complete puzzle
            for thing in rows_cells_boxes:
                if sorted(thing) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                    print('NOPE', thing, rows_cells_boxes.index(thing))
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

        s += 'after ' + str(self.current_iteration) + ' iterations, ' \
             + str(len(self.empties)) + ' empty spots remain\n'
        return s

    @staticmethod
    def get_box(row, cell):
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
                    box = self.get_box(row, cell)

                    possibilities = []

                    for guess in range(1, 10):
                        if guess not in (rows[row] + cells[cell] + boxes[box]):
                            possibilities.append(guess)

                    # print(row, cell)
                    # print('--')
                    # print('row', rows[row])  # your boat
                    # print('col', cells[cell])
                    # print('box', boxes[box])
                    # print('pos', possibilities)
                    # print()

                    self.empties[(row, cell)] = \
                        [rows[row], cells[cell], boxes[box], possibilities]

    def solve(self):  # where the magic happens
        print('NOW AT', self.current_iteration)
        print(self.__str__())
        # print(self.empties[(5, 8)])
        # print('LEFT', self.empties)

        if len(self.empties) > 0 \
                and self.current_iteration < self.max_iterations:
            self.current_iteration += 1

            empty_cells = []
            # to iterate through the dictionary while changing it
            for key in self.empties.keys():
                empty_cells.append(key)

            for empty in empty_cells:  # do stuff to remove possibilities
                current = self.empties[empty]

                # remove possibility if it exists in row, column or box
                possibilities = [i for i in current[3] if i not in
                                 (current[0] + current[1] + current[2])]

                # only one left, put it in the puzzle
                if len(possibilities) == 1:
                    a = possibilities[0]
                    self.sudoku[empty[0]][empty[1]] = possibilities.pop()
                    print(empty, a, 'by cells')
                    self.fill_empties()

            empty_cells = []
            # to iterate through the dictionary while changing it
            for key in self.empties.keys():
                empty_cells.append(key)

            for empty in empty_cells:  # do stuff to remove possibilities
                current = self.empties[empty]

                # remove possibility if it exists in row, column or box
                possibilities = [i for i in current[3] if i not in
                                 (current[0] + current[1] + current[2])]

                # enumerate possibilities per box
                box = self.get_box(empty[0], empty[1])

                if box in self.box_empties.keys():
                    self.box_empties[box].append(empty)
                    self.box_empties[box].append(possibilities)
                else:
                    self.box_empties[box] = [empty, possibilities]

                    # print(self.box_empties)

            vacant_boxes = []

            for key in self.box_empties.keys():
                vacant_boxes.append(key)

            # each box with empty cells
            for vacant in vacant_boxes:
                current = self.box_empties[vacant]  # empty cells in box
                # print('box', vacant, current)

                counts = {}

                # figure out how many times each possibility shows up
                for possibilities in current:
                    if type(possibilities) is list:
                        for each in possibilities:
                            if each not in counts.keys():
                                counts[each] = 0

                        # print(vacant, possibilities)

                        for each in counts.keys():
                            counts[each] += possibilities.count(each)

                for key in counts.keys():
                    if counts[key] == 1:  # only showed up once, has it be it
                        for cell in current:
                            if type(cell) is list and key in cell:
                                coords = current[current.index(cell) - 1]
                                print(coords, key, 'by boxes')
                                self.sudoku[coords[0]][coords[1]] = key
                                self.fill_empties()

                                # remove from current

            self.box_empties = {}
            self.solve()
        else:
            return self.check_puzzle()


if __name__ == '__main__':
    sudoku = Sudoku()
    # print(sudoku)
    if sudoku.get_input():
        sudoku.solve()
        # print(sudoku)
        if sudoku.check_puzzle():
            print('YAY')